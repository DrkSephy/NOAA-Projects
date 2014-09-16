# coding: utf-8
import netCDF4
ds = netCDF4.Dataset("/cephfs/fhs/data/in/acspo/www.star.nesdis.noaa.gov/pub/sod/sst/micros_data/acspo_nc/npp/2014-07-11/ACSPO_V2.30_NPP_VIIRS_2014-07-11_2210-2220_20140714.093352.nc") 
nr, nc = ds.variables["longitude"].shape
long = ds.variables["longitude"]
long[nr//2, nc//2]
