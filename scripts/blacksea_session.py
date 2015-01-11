# coding: utf-8
get_ipython().magic(u'run demo.py')
im
plt.imshow(im)
bit15 = np.array(np.ones(flags.shape)*(2**14), dtype='uint16')
bit16 = np.array(np.ones(flags.shape)*(2**15), dtype='uint16')
bit15
bit15 = np.array(np.ones(flags.shape)*(2**14), dtype='uint16') >0
bit16 = np.array(np.ones(flags.shape)*(2**14), dtype='uint16') >0
bit15
bit15.max()
bit15.min()
bit16.max()
bit16.min()
bit15 = np.array(np.ones(flags.shape)*(2**14), dtype='uint16')
bit16 = np.array(np.ones(flags.shape)*(2**15), dtype='uint16')
bit15.max()
bit15.min()
flags.shape
bit15_mask = np.bitwise_and(flags, bit15)
bit15_mask
bit15_mask.max()
bit15_mask.min()
bit16_mask = np.bitwise_and(flags, bit16)
bit16_mask.min()
bit16_mask.max()
bit15_mask = np.bitwise_and(flags, bit15)>0
bit16_mask = np.bitwise_and(flags, bit16)>0
bit15_mask
bit15_mask.min()
bit15_mask.max()
cloud_mask = bit15_mask and not bit16_mask
cloud_mask = bit15_mask && !(bit16_mask)
cloud_mask = bit15_mask & !(bit16_mask)
cloud_mask = np.logical_and(bit16_mask, np.logical_not(bit15_mask))
cloud_mask
plt.imshow(cloud_mask)
cloud_mask = np.logical_and(bit15_mask, np.logical_not(bit16_mask))
plt.show(cloud_mask)
plt.imshow(cloud_mask)
cloud_mask = np.logical_and(np.logical_notbit15_mask, np.logical_not(bit16_mask))
cloud_mask = np.logical_and(np.logical_not(bit15_mask), np.logical_not(bit16_mask))
plt.imshow(cloud_mask)
cloud_mask = np.logical_and(bit15_mask, bit16_mask)
plt.imshow(cloud_mask)
plt.colorbar()
cloud_mask = np.logical_and(bit16_mask, np.logical_not(bit15_mask))
cloud_mask = np.logical_and(np.logical_not(bit16_mask), (bit15_mask))
clear_mask = np.logical_and(np.logical_not(bit15_mask), np.logical_not(bit16_mask))
plt.imshow(clear_mask)
clear_mask = np.logical_and(np.logical_not(bit16_mask), np.logical_not(bit15_mask))
plt.imshow(clear_mask)
cloud_mask = np.logical_and(np.logical_not(bit16_mask), (bit15_mask))
prob_cloudy = np.logical_and(np.logical_not(bit16_mask), bit15_mask)
bad_mask = np.logical_and(bit16_mask, bit15_mask)
plt.imshow(bad_mask)
plt.imshow(prob_cloudy)
plt.imshow(dt_analysis)
plt.imshow(dt_analysis)
plt.imshow(cloud_mask)
plt.imshow(prob_cloudy)
cloud_mask = np.logical_and((bit16_mask), np.logical_not(bit15_mask))
plt.imshow(cloud_mask)
plt.imshow(land_mask)
plt.figure()
plt.imshow(land_mask)
plt.imshow(cloud_mask)
plt.figure()
plt.imshow(clear_mask)
plt.figure()
plt.imshow(dt_analysis)
plt.clear()
plt.clear
plt.close
plt.close()
plt.close()
land_layer = np.ones(land_mask.shape)
land_layer[np.logical_not(land_mask.nonzero())] = np.NaN
land_layer[np.logical_not(land_mask).nonzero()] = np.NaN
cloud_layer = np.ones(cloud_mask.shape)
prob_cloud_layer = np.ones(prob_cloudy.shape)
cloud_layer[np.logical_not(cloud_mask).nonzero()] = np.NaN
prob_cloud__layer[np.logical_not(prob_cloudy).nonzero()] = np.NaN
prob_cloud_layer[np.logical_not(prob_cloudy).nonzero()] = np.NaN
prob_cloud_layer
cloud_layer
land_layer
masks_layer = np.ones(land_mask.shape)
masks_layer = np.ones(land_mask.shape)*np.NaN
masks_layer
masks_layer[land_mask.nonzero()] = 1 
masks_layer[cloud_mask.nonzero()] = 2
masks_layer[prob_cloudy.nonzero()] = 3
masks_layer
masks_layer[bad_mask.nonzero()] = 4
masks_layer[land_mask.nonzero()] = 1
cmap = matplotlib.colors.ListedColormap(['#A52A2A', 'm', '#808080', 'w'], name='u')
plt.imshow(masks_layer, cmap=cmap)
plt.imshow(masks_layer==2)
plt.imshow(masks_layer==1)
cmap = matplotlib.colors.ListedColormap(['#A52A2A', 'm', 'm', 'm'], name='u')
plt.imshow(masks_layer, cmap=cmap)
cmap = matplotlib.colors.ListedColormap(['#808080', 'm', 'm', 'm'], name='u')
plt.imshow(masks_layer, cmap=cmap)
plt.imshow(masks_layer, cmap=cmap)
plt.imshow(masks_layer, cmap=cmap)
cmap = matplotlib.colors.ListedColormap(['#A0522D', 'm', 'm', 'm'], name='u')
plt.imshow(masks_layer, cmap=cmap)
cmap = matplotlib.colors.ListedColormap(['#A0522D', 'm', '#808080', 'm'], name='u')
plt.imshow(masks_layer, cmap=cmap)
plt.imshow(masks_layer, cmap=cmap)
cmap = matplotlib.colors.from_levels_and_colors([1,2,3,4], ['#A0522D', 'm', '#808080', 'c'], extend=u'neither')
cmap = matplotlib.colors.from_levels_and_colors([1,2,3,4, NaN], ['#A0522D', 'm', '#808080', 'c'], extend=u'neither')
cmap = matplotlib.colors.from_levels_and_colors([1,2,3,4, NaN], ['#A0522D', 'm', '#808080', 'c'], extend=u'neither')
plt.imshow(masks_layer, cmap=cmap)
cmap, norm = matplotlib.colors.from_levels_and_colors([1,2,3,4], ['#A0522D', 'm', '#808080', 'c'])
cmap, norm = matplotlib.colors.from_levels_and_colors([1,2,3,4,NaN], ['#A0522D', 'm', '#808080', 'c'])
plt.imshow(masks_layer, cmap=cmap, norm=norm)
temp = dt_analysis[clear_mask.nonzero()]
temp.max()
temp.min()
clipped_dt = np.clip(dt_analysis, temp.min(), temp.max())
plt.imshow(clipped_dt)
plt.imshow(clipped_dt)
plt.imshow(masks_layer, cmap=cmap, norm=norm)
plt.savefig('blacksea_example.png')
get_ipython().system(u'ls -F --color ')
