#!/usr/bin/env python2

from __future__ import division, print_function, absolute_import

import matplotlib
matplotlib.use('agg')

import mahotas
import matplotlib.pyplot as plt
import numpy as np
import os
import os.path
import shutil
import skimage.morphology
import sys
from matplotlib import colors
from scipy.ndimage.filters import maximum_filter, minimum_filter, \
    median_filter, gaussian_filter
from scipy.ndimage.morphology import binary_erosion, binary_dilation
from scipy.signal import convolve, medfilt
from scipy.spatial import cKDTree

from acspo import NC_ACSPO, ACSPOLocation, ACSPOMiddle, \
    MaskDay, MaskLand, MaskIce, MaskGlint, MaskCloud, MaskCloudClear, \
    MaskCloudProbably, MaskCloudSure
from buffer_20130511_dr1 import Locations as BufLocations
from location import Quadrant
from clear_cold_destriped_nc1 import Locations as ColdLocations
from optimizations import winbinarycomatrix, stdfilt

SSTLow = 270    # was: 271.15
SavefigOpts = dict(bbox_inches='tight', dpi=150)


class BowTie(object):
    def __init__(self, loc):
        lat = loc.read("latitude")
        self.sortind = np.argsort(lat, axis=0)
        if lat[0,0] > lat[-1,0]:
            self.sortind = self.sortind[::-1,:]

        self.acspo = self.sort(loc.read("acspo_mask"))
        self.landmask = (self.acspo & MaskLand) != 0
        self.icemask = (self.acspo & MaskIce) != 0
        self.cloudmask = acspocloud(self.acspo)
        self.cloudmask[self.cloudmask>1] = 1

        self.wdist = self.sort(loc.read("inland_water_to_land_dist"))
        self.rivermask = ~np.isnan(self.wdist) & (self.wdist > 0)

        self.slat = self.sort(lat)
        self.loc = loc

    def sort(self, img):
        assert img.ndim == 2
        return img[self.sortind, np.arange(img.shape[1])]

    def _interp(self, Y, valid, invalid):
        mask = (np.sum(valid, axis=0) >= 2) & \
            np.any(invalid, axis=0)
        for j in np.where(mask)[0]:
            vind, = np.where(valid[:,j])
            iind, = np.where(invalid[:,j])
            u, ui = np.unique(self.slat[vind,j], return_index=True)
            Y[iind,j] = np.interp(self.slat[iind,j], u, Y[vind[ui],j])
        return Y

    def fixacspocloud(self):
        assert np.all((self.cloudmask == -1) | \
            (self.cloudmask == 0) | (self.cloudmask == 1))
        Y = self.cloudmask.astype('f8')
        valid = Y >= 0
        invalid = (Y < 0) & ~self.landmask & ~self.icemask & ~self.rivermask
        return np.ceil(self._interp(Y, valid, invalid)).astype('i')

    def fixfloat64(self, img):
        simg = self.sort(img)
        mimg = medfilt(simg, [3,1])
        newimg = np.copy(img)
        newimg[self.sortind, np.arange(mimg.shape[1])] = mimg

        mask = ~np.isfinite(img)
        newimg[mask] = img[mask]

        Y = self.sort(newimg)
        valid = np.isfinite(Y)
        invalid = np.isnan(Y) & ~self.landmask
        return self._interp(Y, valid, invalid)

    def unsort(self, img):
        u = np.zeros_like(img)
        u[self.sortind, np.arange(u.shape[1])] = img
        return u

    def read(self, name):
        if name == 'latitude':
            return np.copy(self.slat)
        if name == "acspo_mask:night":
            return (self.acspo & MaskDay) == 0
        if name == "acspo_mask:glint":
            return (self.acspo & MaskGlint) != 0
        if name == "acspo_mask:land":
            return np.copy(self.landmask)
        if name == "acspo_mask:ice":
            return np.copy(self.icemask)
        if name == "acspo_mask:cloud":
            return np.copy(self.fixacspocloud())
        if name == "acspo_mask:unfixedcloud":
            return np.copy(self.cloudmask)
        if name == "inland_water_to_land_dist":
            return self.wdist
        if name in ["sst_regression", "brightness_temp_chM12", "brightness_temp_chM15", "brightness_temp_chM16"]:
            return self.fixfloat64(self.loc.read(name))
        if name in ["sst_reynolds", "inland_water_to_land_dist", "ocean_to_land_dist"]:
            return self.sort(self.loc.read(name))
        raise ValueError("unknown variable " + name)

def acspocloud(acspo):
    labels = -1 + np.zeros_like(acspo, dtype='i')
    labels[((acspo&MaskCloud)==MaskCloudClear)] = 0
    labels[((acspo&MaskCloud)==MaskCloudProbably)] = 1
    labels[((acspo&MaskCloud)==MaskCloudSure)] = 2
    return labels


def alg(loc):
    w_c = 10

    bt = BowTie(loc)
    regress = bt.read("sst_regression")
    latitude = bt.read("latitude")
    cloudmask = bt.read("acspo_mask:cloud")


def run_fullgranule():
    if len(sys.argv) < 2:
        print("usage: tempfronts.py filename")
        sys.exit(2)

    name = "R20140819"
    savedir = os.path.join("/cephfs/fhs/data/out/acspo/", name)
    if not os.path.isdir(savedir):
        os.mkdir(savedir)
    loc = NC_ACSPO(sys.argv[1])
    newpath = os.path.join(savedir, name+"_"+os.path.basename(loc.path()))
    if os.path.exists(newpath):
        print(newpath+": output file already exists")
        sys.exit(2)

    print("input file:", sys.argv[1])
    print("output file:", newpath)

    newmask, fronts, _ = alg(loc)
    shutil.copy(loc.path(), newpath)
    try:
        writeacspo(newpath, newmask, fronts)
    except:
        os.unlink(newpath)

def main():
    run_fullgranule()
    #run_crops()

if __name__ == '__main__':
    main()
