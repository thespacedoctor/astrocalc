from __future__ import division
from . import cl_utils
from past.utils import old_div


def luminosity_to_flux(lumErg_S, dist_Mpc):
    """
    *Convert luminosity to a flux*

    **Key Arguments**

    - ``lumErg_S`` -- luminosity in ergs/sec
    - ``dist_Mpc`` -- distance in Mpc


    **Return**

    - ``fluxErg_cm2_S`` -- flux in ergs/cm2/s

    """
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    import numpy as np
    import math
    ## LOCAL APPLICATION ##

    ################ > VARIABLE SETTINGS ######

    ################ >ACTION(S) ################
    # Convert the distance to cm
    distCm = dist_Mpc * MPC_2_CMS
    fluxErg_cm2_S = old_div(lumErg_S, (4 * np.pi * distCm ** 2))

    return fluxErg_cm2_S

##########################################################################
# PRIVATE (HELPER) FUNCTIONS                                                                #
##########################################################################
if __name__ == '__main__':
    main()
