# coding: utf-8
import netCDF4
import numpy as np
ds = netCDF4.Dataset("ACSPO_V2.30_NPP_VIIRS_2014-07-11_2210-2220_20140714.093352.nc", "r+", format="NETCD4")
sst_regression = np.array(ds.variables['sst_regression'])
sst_reynolds = np.array(ds.variables['sst_reynolds'])
anomaly = sst_regression - sst_reynolds
ds.createDimension('columns', 3200)
ds.createDimension('rows', 5408)
v = ds.createVariable('anomaly', 'f4', ('rows', 'columns'))
v[:,:] = anomaly.astype('f4')
new_anomaly = np.array(ds.variables['anomaly'])
new_anomaly
new_anomaly.shape
