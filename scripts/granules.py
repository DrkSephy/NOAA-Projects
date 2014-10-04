# Computes max/min of each granule, spits out new image based on computed range
import netCDF4
import numpy as np
import os
from os.path import isfile, join
from os import listdir

path = "/cephfs/fhs/data/in/acspo/www.star.nesdis.noaa.gov/pub/sod/sst/micros_data/acspo_nc/npp/2014-07-11/"
onlyfiles = [ f for f in listdir(path) if isfile(join(path, f))]

i = 1
for f in onlyfiles:
    dataset = netCDF4.Dataset(path + f)
    min = np.nanmin(dataset.variables['sst_regression'])
    max = np.nanmax(dataset.variables['sst_regression'])
    command = "./cwrender --enhance sst_regression --palette Blue-Red --bitmask acspo_mask/0x4/0x663300 --bitmask acspo_mask/0x20/0xFFFFFF  --bitmask individual_clear_sky_tests_results/0x7FFFFFFF/0x999999 --size 1508   --range " + str(min) + "/" + str(max) + " " + path + f + " " + str(i) + ".png"
    os.system(command)
    i += 1

