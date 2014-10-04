import numpy as np

import netCDF4


# Dataset containing all data

ds = netCDF4.Dataset('ACSPO_V2.30_NPP_VIIRS_2014-07-11_0000-0010_20140714.005638.nc', 'r+', format="NETCD4")

# Dataset containing only Anomaly

ds2 = netCDF4.Dataset('output1.nc')

# Read anomaly

anomaly = np.array(ds2.variables['anomaly'])

# Get rows/columns

nr, nc = ds2.variables['anomaly'].shape

# Create dimensions to store anomaly

ds.createDimension('columns', nc)

ds.createDimension('rows', nr)

v = ds.createVariable('anomaly', 'f4', ('rows', 'columns'))
v[:,:] = anomaly.astype('f4')

sst = ds.variables['sst_regression']
sst[:, :] = v[:, :]