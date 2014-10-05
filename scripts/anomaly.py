import netCDF4
import numpy as np
from os import listdir
from os.path import isfile, join

# Path to NC files containing all data
orig_path = "/home/DrkSephy/tmp/nc/"
orig_files = [ f for f in listdir(orig_path) if isfile(join(orig_path, f)) ]

# List of all files containing only anomaly
anomaly_path = "/home/DrkSephy/csdirs-spt/anomaly/"
# List of all the files in order
anomaly_files =   ['output1.nc',
         'output2.nc',
         'output3.nc',
         'output4.nc',
         'output5.nc',
         'output6.nc',
         'output7.nc',
         'output8.nc',
         'output9.nc',
         'output10.nc',
         'output11.nc',
         'output12.nc',
         'output13.nc',
         'output14.nc',
         'output15.nc',
         'output16.nc',
         'output17.nc',
         'output18.nc',
         'output19.nc',
         'output20.nc',
         'output21.nc',
         'output22.nc',
         'output23.nc',
         'output24.nc',
         'output25.nc',
         'output26.nc',
         'output27.nc',
         'output28.nc',
         'output29.nc',
         'output30.nc',
         'output31.nc',
         'output32.nc',
         'output33.nc',
         'output34.nc',
         'output35.nc',
         'output36.nc',
         'output37.nc',
         'output38.nc',
         'output39.nc',
         'output40.nc',
         'output41.nc',
         'output42.nc',
         'output43.nc',
         'output44.nc',
         'output45.nc',
         'output46.nc',
         'output47.nc',
         'output48.nc',
         'output49.nc',
         'output50.nc',
         'output51.nc',
         'output52.nc',
         'output53.nc',
         'output54.nc',
         'output55.nc',
         'output56.nc',
         'output57.nc',
         'output58.nc',
         'output59.nc',
         'output60.nc',
         'output61.nc',
         'output62.nc',
         'output63.nc',
         'output64.nc',
         'output65.nc',
         'output66.nc',
         'output67.nc',
         'output68.nc',
         'output69.nc',
         'output70.nc',
         'output71.nc',
         'output72.nc',
         'output73.nc',
         'output74.nc',
         'output75.nc',
         'output76.nc',
         'output77.nc',
         'output78.nc',
         'output79.nc',
         'output80.nc',
         'output81.nc',
         'output82.nc',
         'output83.nc',
         'output84.nc',
         'output85.nc',
         'output86.nc',
         'output87.nc',
         'output88.nc',
         'output89.nc',
         'output90.nc',
         'output91.nc',
         'output92.nc',
         'output93.nc',
         'output94.nc',
         'output95.nc',
         'output96.nc',
         'output97.nc',
         'output98.nc',
         'output99.nc',
         'output100.nc',
         'output101.nc',
         'output102.nc',
         'output103.nc',
         'output104.nc',
         'output105.nc',
         'output106.nc',
         'output107.nc',
         'output108.nc',
         'output109.nc',
         'output110.nc',
         'output111.nc',
         'output112.nc',
         'output113.nc',
         'output114.nc',
         'output115.nc',
         'output116.nc',
         'output117.nc',
         'output118.nc',
         'output119.nc',
         'output120.nc',
         'output121.nc',
         'output122.nc',
         'output123.nc',
         'output124.nc',
         'output125.nc',
         'output126.nc',
         'output127.nc',
         'output128.nc',
         'output129.nc',
         'output130.nc',
         'output131.nc',
         'output132.nc',
         'output133.nc',
         'output134.nc',
         'output135.nc',
         'output136.nc',
         'output137.nc',
         'output138.nc',
         'output139.nc',
         'output140.nc',
         'output141.nc',
         'output142.nc',
         'output143.nc',
         'output144.nc'
        ]

i = 0
# Iterate over all the .nc files we want to change regression
for f in orig_files:
    # Original Dataset
    ds = netCDF4.Dataset(orig_path + f, 'r+', format="NETCD4")
    # Anomaly Dataset
    ds2 = netCDF4.Dataset(anomaly_path + anomaly_files[i])
    #Read anomaly
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
    # print "[" + str(i) + "]" + " " + orig_path + f + " " + anomaly_path + anomaly_files[i] 
    i += 1

