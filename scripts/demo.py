# coding: utf-8
from pyhdf.SD import SD, SDC
f = SD('outblacksea.hdf', SDC.READ)
x = f.select('sea_surface_temperature')
im = x[:,:]
from matplotlib import pyplot as plt
plt.imshow(im)
f.datasets()
dt_analysis = f.select('dt_analysis')
import numpy as np
dt_analysis = np.array(dt_analysis[:,:]*0.1)
dt_analysis
dt_analysis = np.array(dt_analysis[:,:]*0.1)
plt.imshow(dt_analysis)
flags = f.select('l2p_flags')
flags = np.array(flags[:,:], dtype='uint16')
flags
flags.max()
flags.min()
flags.shape
land_select = np.array(np.ones(flags.shape)*2, dtype='uint16')
land_select
land_mask = np.bitwise_and(flags, land_select)
land_mask
land_mask.max()
land_mask.min()
im2 = land_mask
plt.imshow(im2)
plt.imshow(im)
