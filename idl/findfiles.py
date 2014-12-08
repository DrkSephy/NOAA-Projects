# findfiles.py
# ------------
#
# Re-implementation of findfiles.ksh
# Re-implementation of findfiles.pro

#------------------------
#     findfiles.ksh
#------------------------


def getSatellite(satellite):
    # Sets input_dir based on satellite
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
    pass
