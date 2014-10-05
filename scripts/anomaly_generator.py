# Builds images showing Anomaly (sst_regression - sst_reynolds)
import netCDF4
import numpy as np
import os
from os.path import isfile, join
from os import listdir

orig_path = "/home/DrkSephy/tmp/nc/"
orig_files = [ f for f in listdir(orig_path) if isfile(join(orig_path, f)) ]

i = 1
for f in onlyfiles:
    command = "cwrender --enhance sst_regression --palette Blue-Red --size 1508 --range -4/4" + " " + path + f + " " +  str(i) + ".png"
    os.system(command)
    i += 1

