# This file contains commands for further processing
# of granules using CDAT (cwmath).

import numpy as np
from pyhdf.SD import SD, SDC
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join
from subprocess import Popen, PIPE

file = 
# Read a granule in
ds = SD(file, SDC.READ)
# Grab l2p_flags dataset
flags = ds.select('l2p_flags')
flags = np.array(flags[:,:], dtype='uint16')

# Grab bit 15
bit15 = np.array(np.ones(flags.shape)*(2**14), dtype='uint16')
# Grab bit 16
bit16 = np.array(np.ones(flags.shape)*(2**15), dtype='uint16')
# Get bit 15 mask
bit15_mask = np.bitwise_and(flags, bit15)>0
# Get bit 16 mask
bit16_mask = np.bitwise_and(flags, bit16)>0


# Command 1: sea_surface_temperature
sst = 'cwmath --verbose --template sea_surface_temperature --expr ' + ' ' + '''"sea_surface_temperature = sea_surface_temperature"''' + ' ' + file + ' ' + 'math.hdf'

# Command 2: dt_analysis
dt_analysis = 'cwmath --verbose --template dt_analysis --expr' + ' ' + '''"dt_analysis = sea_surface_temperature"''' + ' ' + file + ' ' + 'math.hdf'

# Command 3: Create missing flag
missing_flag = 'cwmath --verbose --template sea_surface_temperature --expr' + ' ' +  '''"missing_flag = select ( and (l2p_flags, 49152) == 49152, 1., 0. )"''' +  ' ' + file + ' ' + 'math.hdf'

# Command 4: Create cloud flag
cloud_flag = 'cwmath --verbose --template sea_surface_temperature --expr' + ' ' +  '''"cloud_flag = select (and (l2p_flags, 49152) < 16384, 0., 1.)"''' + ' ' + file + ' ' + 'math.hdf'

# Command 5: Create glint flag
glint_flag = 'cwmath --verbose --template sea_surface_temperature --expr' + ' ' + '''"glint_flag = select ( (and (l2p_flags, 8192) == 8192), 1., 0.)"''' + ' ' + file + ' ' + 'math.hdf'


cmds = []
cmds.append(sst)
cmds.append(dt_analysis)
cmds.append(missing_flag)
cmds.append(cloud_flag)
cmds.append(glint_flag)

for command in cmds:
    #print command
    pid = Popen(cmd, shell=True)
    pid.wait()



