# findfiles.py
# ------------
#
# Re-implementation of findfiles.ksh
# Re-implementation of findfiles.pro

import numpy as np 
import netCDF4
from os import listdir
from os.path import isfile, join


#------------------------
#     findfiles.ksh
#------------------------


def getSatellite(satellite):
    # Parameters:
    #   * satellite: String
    #       - Satellite name
    # Returns:
    #   * input_dir: String
    #       - input directory of files
    input_dir = ''
    if satellite == 'NOAA16_GHRR':
        input_dir = 'gpnl'
    elif satellite == 'NOAA17_GHRR':
        input_dir = 'gpnm'
    elif satellite == 'NOAA18_GHRR':
        input_dir = 'gpnn'
    elif satellite == 'NOAA19_GHRR':
        input_dir = 'gpnp'
    elif satellite == 'METOPA_GHRR':
        input_dir = 'gpm2'
    elif satellite == 'METOPA_FRAC':
        input_dir = 'frac'
    return input_dir

#------------------------
#     findfiles.pro
#------------------------

# Main script
def findFiles(path):
    # Parameters:
    #   * input_dir: String
    #       - input directory of files
    #   * satellite: String
    #       - Name of satellite/data type
    #   * mmdd: String
    #       - Month/Day of file
    
    # Number of special regions
    numRegions = 5 
    openDay = np.zeros(numRegions)
    openNight = np.zeros(numRegions)
    iunDay = np.arange(numRegions)
    iunDay = iunDay + 10 
    iunNight = iunDay[numRegions - 1] + iunDay + 1 

    # List containing all special regions
    regionName = ['MR', 'ER', 'SR', 'WN', 'BS']
    # Path of files to look into
    # path = input_dir + '_' +  satellite + '_' +  mmdd + '.hdf'
    # Need to get a regex to sort files inside the right directory
    # TODO: FIND REGEX 
    # filterFiles(path)
    files = [ f for f in listdir(path) if isfile(join(path, f)) ]
    print files




# Not really necessary right now
def filterFiles(path):
    # Returns all files within a given path matching the format
    files = [ f for f in listdir(path) if isfile(join(path, f)) ]
    # For all the files in the given directory, filter out the right ones
    for f in files:
        pass
    



numRegions = 5 
openDay = np.zeros(numRegions)
openNight = np.zeros(numRegions)
iunDay = np.arange(numRegions)
iunDay = iunDay + 10 
iunNight = iunDay[numRegions - 1] + iunDay + 1 

# List containing all special regions
regionName = ['MR', 'ER', 'SR', 'WN', 'BS']
# Path of files to look into
# path = input_dir + '_' +  satellite + '_' +  mmdd + '.hdf'
# Need to get a regex to sort files inside the right directory
# TODO: FIND REGEX 
# filterFiles(path)
path = "/Users/DrkSephy/Dropbox/granules/"
files = [ f for f in listdir(path) if isfile(join(path, f)) ]
print files