# findfiles.py
# ------------
#
# Re-implementation of findfiles.ksh
# Re-implementation of findfiles.pro

import numpy as np 

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

def findFiles(input_dir, satellite, mmdd):
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
    
