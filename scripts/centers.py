# Script for computing longitude and latitude centers of granules

import netCDF4
from os import listdir
from os.path import isfile, join

path = "/cephfs/fhs/data/in/acspo/www.star.nesdis.noaa.gov/pub/sod/sst/micros_data/acspo_nc/npp/2014-07-11/"
onlyfiles = [ f for f in listdir(path) if isfile(join(path, f)) ]
computedData = [ ]

# Begin computation loop
for f in onlyfiles:
    dataset = netCDF4.Dataset(path + f)
    nr, nc = dataset.variables["latitude"].shape
    lat = dataset.variables["latitude"]
    latitude = lat[nr//2, nc//2]
    numr, numc = dataset.variables["longitude"].shape
    long = dataset.variables["longitude"]
    longitude = long[numr//2, numc//2]
    computedData.append({ 'Latitude': latitude, 'Longitude': longitude })

print len(computedData)
print computedData
