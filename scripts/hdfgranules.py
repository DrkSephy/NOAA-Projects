from pyhdf.SD import SD, SDC

f = SD('MOD021KM.A2014295.2340.005.2014296093338.hdf', SDC.READ)
# print all datasets
f.datasets()
# Get a handle to specific datasets
ff = f.select('Longitude')
# print out datasets
ff[:,:]
