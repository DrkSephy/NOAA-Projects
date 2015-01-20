# findfiles.py
# ------------
#
# Re-implementation of findfiles.ksh
# Re-implementation of findfiles.pro

import yaml
import netCDF4
import numpy as np  
from os import listdir
from os.path import isfile, join
from subprocess import Popen, PIPE


# List containing all special regions
regionName = ['MR', 'ER', 'SR', 'WN', 'BS']

# Create global data structure which has a list for each 
data = { name: [] for name in regionName }
daynightData = { }
daynightData['day'] = { name: [] for name in regionName }
daynightData['night'] = { name: [] for name in regionName }


def intersection(path, masterPath):
    # path - string
    #    The path to granules to be processed
    # masterPath - string
    #    The path to the master files for registration

    # Special regions bounding box
    specialRegions = {
        'MR': {'lonmin': 98, 'lonmax': -82, 'latmin': 18, 'latmax': 30, 'master': masterPath + 'MASTER_MR_1KM.hdf'  },
        'ER': {'lonmin': -80, 'lonmax': -61, 'latmin': 30, 'latmax': 47, 'master': masterPath + 'MASTER_ER_1KM.hdf' },
        'SR': {'lonmin': -89, 'lonmax': -72, 'latmin': 22, 'latmax': 38, 'master': masterPath + 'MASTER_SR_1KM.hdf' },
        'WN': {'lonmin': -136, 'lonmax': -121, 'latmin': 39, 'latmax': 51, 'master': masterPath + 'MASTER_WN_1KM.hdf'},
        'BS': {'lonmin': 27, 'lonmax': 42, 'latmin': 40, 'latmax': 48, 'master': masterPath + 'MASTER_BS_1KM.hdf'}
    }

    # Add the path to your granules here
    # path = "/Users/DrkSephy/Desktop/January/"
    fileList = [ f for f in listdir(path) if isfile(join(path, f)) ]
    # Add your path to the master region files here
    # masterPath = "/home/DrkSephy/special_regions/testing/master_files/"


    # Loop over all granules inside fileList
    for f in fileList: 
        ds = netCDF4.Dataset(path + f)
        # Select l2p_flags variable
        flags = np.array(ds.variables['l2p_flags'])
        # Read day/night bit (bit 10: 0=night, 1=day)
        bit10 = np.array(np.ones(flags.shape)*(2**9), dtype='uint16')
        # Create array of all day pixels 
        dayMask = np.squeeze(np.bitwise_and(flags, bit10) > 0)
        # Create array of all night pixels
        nightMask = np.bitwise_not(dayMask)

        # Grab the longitude
        lon = np.array(ds.variables['lon']) 

        # Grab the latitude
        lat = np.array(ds.variables['lat'])

        # Iterate over each special region
        # Get the maximum number of pixels bounded in the region
        maxRegion = 0
        # Which region had the most bounded pixels?
        maxRegionName = ''

        for reg in regionName:
            # Create an array of records in the file which are  
            # within the special region
            region_arr = (np.logical_and(np.logical_and(lon >= specialRegions[reg]['lonmin'], lon <= specialRegions[reg]['lonmax']),
                            np.logical_and(lat >= specialRegions[reg]['latmin'], lat <= specialRegions[reg]['latmax']))).nonzero()

            dayCount = len(dayMask[region_arr].nonzero()[0])
            nightCount = len(nightMask[region_arr].nonzero()[0])
            if dayCount > 0: 
                daynightData['day'][reg].append((f, specialRegions[reg]['master'], dayCount, 'day'))
            if nightCount > 0:
                daynightData['night'][reg].append((f, specialRegions[reg]['master'], nightCount, 'night'))

# Process the granules
intersection("/Users/DrkSephy/Desktop/January/", "/home/DrkSephy/special_regions/testing/master_files/")

# Generates commands to build master files
def commandGeneration(path):
    # path: string
    #   - The input path of the granule list.
    #     Used for appending to registered file name.
    granuleList = yaml.dump(daynightData)
    granuleData = yaml.load(granuleList)


    # Figure out which region has the maximum number of pixels for that region. 
    # That is the granule we want to process. 
    max = 0
    cmds = []
    # Iterate over day/night granule entries
    for d in granuleData:
        for region in granuleData[d]:
            if granuleData[d][region] != []: 
                # print granuleData[d][region]
                # Loop over each array of entries
                for val in granuleData[d][region]:
                    # Get the max value
                    if val[2] > max:
                        max = val[2]
                        masterfile = val[1]
                        granuleName = val[0]
                        daynight = val[3]
                max = 0
                # Register the file
                cmd = 'cwregister' + ' ' + masterfile + ' ' + path + granuleName + ' ' + 'reg' + daynight + region + val[0][:-3]  + '.hdf'
                cmds.append(cmd)

    return cmds

# Process the granules
intersection("/Users/DrkSephy/Desktop/January/", "/home/DrkSephy/special_regions/testing/master_files/")
# Package data in YAML
commands = commandGeneration("/Users/DrkSephy/Desktop/January/")

# Execute all CWregister commands
for cmd in commands: 
    pid = Popen(cmd, shell=True)
    pid.wait()


















