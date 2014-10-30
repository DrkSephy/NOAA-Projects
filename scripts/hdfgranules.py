from os import listdir
from os.path import isfile, join
from pyhdf.SD import SD, SDC

path = "/home/DrkSephy/terra"
onlyfiles = [ f for f in listdir(path) if isfile(join(path, f)) ]
computedData = [ ]

# Begin computation loops
for f in onlyfiles:
    dataset = SD(path + f, SDC.READ)
    # Get longitude
    lo = f.select('Longitude')
    nr, nc = lo[:,:].shape
    long = lo[:,:]
    longitude = long[nr//2, nc//2]

    # Get latitude
    la = f.select('Latitude')
    numr, numc = la[:,:].shape
    lat = la[:,:]
    latitude = lat[numr//2, numc//2]
    computedData.append({'Latitude': latitude, 'Longitude': longitude})

print computedData
