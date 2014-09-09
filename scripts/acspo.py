#!/usr/bin/env python2

from __future__ import print_function, division

import netCDF4
import numpy as np
from datetime import datetime

MaskInvalid       = (1<<0)           # or Valid
MaskDay           = (1<<1)           # or Night
MaskLand          = (1<<2)           # or Ocean
MaskTwilightZone  = (1<<3)           # or No Twilight Zone
MaskGlint         = (1<<4)           # or No Sun Glint
MaskIce           = (1<<5)           # or No Ice

MaskCloudOffset   = 6               # first bit of cloud mask
MaskCloud         = (1<<7)|(1<<6)
MaskCloudClear    = 0               # 0 - Clear
MaskCloudProbably = (1<<6)          # 1 - Probably cloudy
MaskCloudSure     = (1<<7)          # 2 - Confidently  cloudy
MaskCloudInvalid  = (1<<7)|(1<<6)   # 3 - Irrelevant to SST (which includes land, ice and invalid pixels)

class NC_ACSPO(object):
    def __init__(self, filename, mode='r', orient=False):
        """filename -- full path to netcdf4 file
        mode -- r+ for read/write
        """
        self.filename = filename
        self.ds = netCDF4.Dataset(filename, mode)
        self.orient = orient
        self._mode = mode

    def close(self):
        self.ds.close()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "NC_ACSPO(%s, mode=%s, orient=%s)" % (
            repr(self.filename), repr(self._mode), self.orient)

    def setorient(self, ok):
        self.orient = ok

    def starttime(self):
        return datetime.strptime(self.ds.TIME_COVERAGE_START, "%Y-%m-%dT%H:%M:%SZ")

    def endtime(self):
        return datetime.strptime(self.ds.TIME_COVERAGE_END, "%Y-%m-%dT%H:%M:%SZ")

    def read(self, vname, ind=None):
        """Read data.
        vname -- Variable instance
        ind -- 2D slice
        """
        if ind is None:
            ind = np.s_[:,:]
        img = self.ds.variables[vname][ind]
        if img.dtype == np.dtype('f4'):
            img = np.array(img, dtype='f8')
        if self.orient:
            lat = self.ds.variables['latitude']
            lon = self.ds.variables['longitude']
            if lat[0,0] < lat[-1,-1]:
                img = img[::-1,:]
            if lon[0,0] > lon[-1,-1] or ((lon[0,0] < -90) and lon[-1,-1] > 90):
                img = img[:,::-1]
        return img

    def needsorient(self):
        lat = self.ds.variables['latitude']
        lon = self.ds.variables['longitude']
        return lat[0,0] < lat[-1,-1] or \
            (lon[0,0] > lon[-1,-1] or ((lon[0,0] < -90) and lon[-1,-1] > 90))

    def shape(self, vname=None):
        if vname is not None:
            return self.ds.variables[vname].shape
        dims = self.ds.dimensions
        return len(dims['scan_lines_along_track']), len(dims['pixels_across_track'])

    def writeprob(self, img):
        """Write clear_probability.
        img -- 2D array
        """
        cp = self.ds.createVariable("clear_probability", "f4",
                ("scan_lines_along_track", "pixels_across_track"),
                zlib=True, complevel=1, shuffle=True,
                chunksizes=self.ds.variables["sst_regression"].chunking())
        cp[:,:] = img.astype('f4')
        cp.UNITS = "none"
        cp.Description = 'Probability of absence of cloud from Logistic Regression'

    def writestatacspo(self, mask):
        acspo = self.ds.createVariable("stat_acspo_mask", "u1",
                ("scan_lines_along_track", "pixels_across_track"),
                zlib=True, complevel=1, shuffle=True,
                chunksizes=self.ds.variables["acspo_mask"].chunking())
        acspo[:,:] = mask.astype("u1")
        acspo.UNITS = "none"
        acspo.Description = "ACSPO mask packed into 1 byte: bits1-2 (00=clear; 01=probably clear; 10=cloudy; 11=clear-sky mask undefined); bit3 (1=water front; 0=not water front); bit4-8 (unused)"

    def path(self):
        return self.filename

    def full(self):
        return NC_ACSPO(self.filename)

    def middle(self):
        return ACSPOMiddle(self.filename)


class ACSPOLocation(NC_ACSPO):
    def __init__(self, filename, fov=None, scans=None, sstrange=None):
        self.g = super(ACSPOLocation, self)
        self.g.__init__(filename)
        self.fov = fov
        self.scans = scans
        self.sstrange = sstrange

    def __repr__(self):
        return "ACSPOLocation(%s, fov=%s, scans=%s)" % (
            repr(self.path()), self.fov, self.scans)

    def read(self, vname):
        ind = np.s_[self.scans[0]:self.scans[1],
            self.fov[0]:self.fov[1]]
        return self.g.read(vname, ind)

class ACSPOMiddle(NC_ACSPO):
    def __init__(self, filename):
        self.g = super(ACSPOMiddle, self)
        self.g.__init__(filename)
        self.ind = np.s_[:,1008:2192]

    def __repr__(self):
        return "ACSPOMiddle(%s)" % (repr(self.path()),)

    def read(self, vname):
        return self.g.read(vname, self.ind)
