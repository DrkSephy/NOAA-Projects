import numpy as np
import matplotlib.pyplot as plt

np.ones((1024,1024))
np.ones((1024,1024))*np.nan
im = np.ones((1024,1024))*np.nan
for i, line in ascfile:
    im[i] = np.array(list(line)[:-1]).astype('int')
for line in ascfile:
    list(line)
    break
ascfile
ascfile.split("\n")
ascfile.split("\n")[:-1]
for i, line in enumerate(ascfile.split("\n")[:-1]):
    im[i] = np.array(list(line)).asarray(int)
for i, line in enumerate(ascfile.split("\n")[:-1]):
             im[i] = np.array(list(line)).astype(int)
im
np.unique(im)