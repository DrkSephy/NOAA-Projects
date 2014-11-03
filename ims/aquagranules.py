from os import listdir
from os.path import isfile, join
from pyhdf.SD import SD, SDC

# path = "/home/DrkSephy/terra/"
path = "/home/DrkSephy/aqua/HKM/"
onlyfiles = [ f for f in listdir(path) if isfile(join(path, f)) ]
computedData = [ ]

# Begin computation loops
for f in onlyfiles:
    print "Processing file: " + f
    dataset = SD(path + f, SDC.READ)
    # Get longitude
    lo = dataset.select('Longitude')
    nr, nc = lo[:,:].shape
    long = lo[:,:]
    longitude = long[nr//2, nc//2]
    # Get latitude
    la = dataset.select('Latitude')
    numr, numc = la[:,:].shape
    lat = la[:,:]
    latitude = lat[numr//2, numc//2]
    computedData.append({'Latitude': latitude, 'Longitude': longitude, 'Satellite': 'Aqua', 'File': f})

print computedData
