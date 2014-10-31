import os
from os.path import isfile, join
from os import listdir

path = "/home/DrkSephy/aqua/HKM/"
onlyfiles = [ f for f in listdir(path) if isfile(join(path, f))]

i = 1
for f in onlyfiles:
    command = "qir " + f