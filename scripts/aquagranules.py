from pyhdf.SD import SD, SDC

def process(file):
    dataset = SD(file, SDC.READ)
    lo = dataset.select('Longitude')
    nr, nc = lo[:,:].shape
    long = lo[:,:]
    longitude = long[nr//2, nc//2]
    # Get latitude
    la = dataset.select('Latitude')
    numr, numc = la[:,:].shape
    lat = la[:,:]
    latitude = lat[numr//2, numc//2]
    print {'Longitude': longitude, 'Latitude': latitude, 'Satellite': 'Aqua'}

process('MYD021KM.A2014295.2355.005.2014296204732.hdf')


