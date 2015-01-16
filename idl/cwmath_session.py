# coding: utf-8
from pyhdf.SD import SD, SDC
ds = SD('regdayBS20141122085952-STAR-L2P_GHRSST-SST1m-GHRR_METOPA-v02.0-fv01.0.hdf', SDC.READ)
from matplotlib import pyplot as plt
import numpy as np
flags = ds.select('l2p_flags')
flags
flags = np.array(flags[:,:], dtype='uint16')
flags
plt.imshow(flags)
bit15_mask = np.bitwise_and(flags, bit15)>0
bit15 = np.array(np.ones(flags.shape)*(2**14), dtype='uint16')
bit16 = np.array(np.ones(flags.shape)*(2**15), dtype='uint16')
bit15_mask = np.bitwise_and(flags, bit15)>0
bit16_mask = np.bitwise_and(flags, bit16)>0
missing = np.logical_and(bit15_mask, bit16_mask)
missing
np.min(missing)
plt.imshow(missing)
newds = SD('testmissing.hdf', SDC.READ)
newds.datasets()
new = newds.select('missing_flag')
im2 = new[:,:]
plt.imshow(im2)
plt.imshow(im)
plt.imshow(flags)
plt.imshow(missing)
plt.imshow(missing)
plt.imshow(im2)
plt.imshow(missing)
cloud_flag = np.logical_and(bit16_mask, np.logical_not(bit15_mask))
plt.imshow(cloud_flag)
cloud_flag
plt.imshow(cloud_flag)
math = SD('outmath2', SDC.READ)
math = SD('outmath2.hdf', SDC.READ)
math.datasets()
data = math.select('cloud_flag')
plt.imshow(data)
newdata = data[:,:]
plt.imshow(newdata)
plt.imshow(newdata)
np.shape(cloud_flag)
math = SD('outmath3.hdf', SDC.READ)
math.datasets()
data = math.select('cloud_flag')
newdata = data[:,:]
plt.imshow(newdata)
math = SD('outmath4.hdf', SDC.READ)
math.datasets()
data = math.select('cloud_flag')
newdata = data[:,:]
plt.imshow(newdata)
plt.imshow(newdata)
non_clear = np.logical_not(np.logical_or(bit16_mask, bit15_mask))
plt.imshow(non_clear)
math = SD('outmath6.hdf', SDC.READ)
data = math.select('cloud_flag')
newdata = data[:,:]
plt.imshow(newdata)
math = SD('outmath7.hdf', SDC.READ)
data = math.select('cloud_flag')
newdata = data[:,:]
plt.imshow(newdata)
figure()
plt.imshow(non_clear)
grey()
gray()
math = SD('out10.hdf', SDC.READ)
data = math.select('cloud_flag')
newdata = data[:,:]
plt.imshow(newdata)
plt.imshow(newdata)
sst = SD('sst.hdf', SDC.READ)
sst_data = sst.select('sea_surface_temperature')
sst.datasets()
missing_flag = SD('sst.hdf', SDC.READ)
missing_flag.datasets()
missing_data = missing_flag('missing_flag')
missing_flag.datasets()
dataset = missing_flag.select('missing_flag')
plt.imshow(dataset)
d = dataset[:,:]
plt.imshow(d)
bit13 = np.array(np.ones(flags.shape)*(2**12), dtype='uint16')
bit13_mask = np.bitwise_and(flags, bit13)
bit13_mask = np.bitwise_and(flags, bit13) > 0
plt.imshow(bit13_mask)
2**13
glint = SD('glint.hdf', SDC.READ)
glint.datasets()
glint_data = glint.select('glint_flag')
plt.imshow(glint_data)
glintData = glint_data[:,:]
plt.imshow(glintData)
plt.imshow(glintData)
