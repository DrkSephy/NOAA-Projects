# coding: utf-8
import netCDF4
path = "/cephfs/fhs/data/in/acspo/www.star.nesdis.noaa.gov/pub/sod/sst/micros_data/acspo_nc/npp/2014-07-11/"
path
from os import listdir
from os.path import isfile, join
onlyfiles = [ f for f in listdir(path) if isfile(join(path, f))]
onlyfiles
