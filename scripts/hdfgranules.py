from pyhdf.SD import SD, SDC

f = SD('MOD021KM.A2014295.2340.005.2014296093338.hdf', SDC.READ)
# print all datasets
f.datasets()
# Get a handle to specific datasets
lo = f.select('Longitude')
# print out datasets
lo[:,:]
# Get number of rows/columns
nr, nc = lo[:,:].shape
long = lo[:,:]
longitude = long[nr//2, nc//2]

la = f.select('Latitude')
numr, numc = la[:,:].shape
lat = la[:,:]
latitude = lat[numr//2, numc//2]