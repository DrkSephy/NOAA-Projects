from glasslab_cluster.io import modis
import numpy as np
from scipy import misc

def gen_fc(fname, bands):

    hdf = modis.Level1B(fname)
    bs = []
    for band in bands:
        b = hdf.reflectance(band).read()
        b[b>1] = 1
        b = (b-np.nanmin(b))/(np.nanmax(b)-np.nanmin(b))
        bs.append(b)

    return np.dstack(bs)



hdf = 'QIR.MYD02HKM.A2014295.0050.005.2014295171106.hdf'
bands = [3,6,7]

fc = gen_fc(hdf,bands)
misc.imsave('%s.png'%hdf[:-4],np.round(fc*255).astype('uint8'))


