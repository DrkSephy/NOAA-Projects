# Script for reading variables from netCDF files

import netCDF4
import numpy as np

dataset = netCDF4.Dataset("/cephfs/fhs/data/in/acspo/www.star.nesdis.noaa.gov/pub/sod/sst/micros_data/acspo_nc/npp/2014-07-11/ACSPO_V2.30_NPP_VIIRS_2014-07-11_2210-2220_20140714.093352.nc") 
dataset.variables["latitude"].shape
# Out: (5408, 3200)
nr, nc = dataset.variables["latitude"].shape
lat = dataset.variables["latitude"]
lat[nr//2, nc//2]
# Out: 14.461406

# Reading SST variables
sst = np.array(dataset.variables["latitude"])