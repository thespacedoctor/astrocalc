

def luminosity_to_flux(lumErg_S, dist_Mpc):
    """
    *Convert luminosity to a flux*

    **Key Arguments:**
        - ``lumErg_S`` -- luminosity in ergs/sec
        - ``dist_Mpc`` -- distance in Mpc

    **Return:**
        - ``fluxErg_cm2_S`` -- flux in ergs/cm2/s
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    import numpy as np
    import math
    ## LOCAL APPLICATION ##

    ################ > VARIABLE SETTINGS ######

    ################ >ACTION(S) ################
    # Convert the distance to cm
    distCm = dist_Mpc * MPC_2_CMS
    fluxErg_cm2_S = lumErg_S / (4 * np.pi * distCm ** 2)

    return fluxErg_cm2_S


def getDateFromMJD(mjd):
    """*convert mjd to a date*"""
    import math
    from datetime import datetime
    unixtime = (mjd + 2400000.5 - 2440587.5) * 86400.0
    theDate = datetime.utcfromtimestamp(unixtime)
    return theDate.strftime("%Y-%m-%d %H:%M:%S.%f")


def getSQLDateFromMJD(mjd):
    """*convert mjd to a date*"""
    import math
    from datetime import datetime
    unixtime = (mjd + 2400000.5 - 2440587.5) * 86400.0
    theDate = datetime.utcfromtimestamp(unixtime)
    return theDate.strftime("%Y-%m-%dT%H:%M:%S.%f")

# 2012-03-26 KWS Added function to convert from date to MJD


def getMJDFromSqlDate(sqlDate):
    """*convert a sql date to mjd*"""
    import math
    import time
    mjd = None
    sqlDate = str(sqlDate)

    try:
        year, month, day = sqlDate[0:10].split('-')
        hours, minutes, seconds = sqlDate[11:19].split(':')
        t = (int(year), int(month), int(day), int(hours),
             int(minutes), int(seconds), 0, 0, 0)
        unixtime = int(time.mktime(t))
        mjd = unixtime / 86400.0 - 2400000.5 + 2440587.5
    except ValueError, e:
        mjd = None
        print "String is not in SQL Date format."

    return mjd


def getDateFractionMJD(mjd):
    """*convert mjd to date fraction*"""
    import math
    unixtime = (mjd + 2400000.5 - 2440587.5) * 86400.0
    theDate = datetime.utcfromtimestamp(unixtime)
    dateString = theDate.strftime("%Y:%m:%d:%H:%M:%S")
    (year, month, day, hour, min, sec) = dateString.split(':')
    dayFraction = int(day) + int(hour) / 24.0 + int(min) / \
        (24.0 * 60.0) + int(sec) / (24.0 * 60.0 * 60.0)
    dateFraction = "%s %s %05.2f" % (year, month, dayFraction)
    return dateFraction


def coords_sex_to_dec(ra, dec):
    """*Convert sexagesimal ra and dec to decimal degrees*"""
    import dryxPython.astrotools.dec_sexegesimal_to_decimal
    import dryxPython.astrotools.ra_sexegesimal_to_decimal
    import math
    dec = dec_sexegesimal_to_decimal.dec_sexegesimal_to_decimal(
        dec)

    ra = ra_sexegesimal_to_decimal.ra_sexegesimal_to_decimal(ra)

    return ra, dec


def calculate_cartesians(ra, dec):
    """*Convert decimal degrees ra and dec to cartesians*"""
    import math
    ra = math.radians(ra)
    dec = math.radians(dec)
    cos_dec = math.cos(dec)
    cx = math.cos(ra) * cos_dec
    cy = math.sin(ra) * cos_dec
    cz = math.sin(dec)

    cartesians = (cx, cy, cz)
    return cartesians


def getAngularSeparation(ra1, dec1, ra2, dec2):
    """
    *Calculate the angular separation between two objects.  If either set of
    coordinates contains a colon, assume it's in sexagesimal and automatically
    convert into decimal before doing the calculation.*
    """
    import dryxPython.astrotools as dat
    import math

    if ':' in str(ra1):
        ra1 = dat.ra_sexegesimal_to_decimal.ra_sexegesimal_to_decimal(ra1)
    if ':' in str(dec1):
        dec1 = dat.dec_sexegesimal_to_decimal.dec_sexegesimal_to_decimal(
            dec1)
    if ':' in str(ra2):
        ra2 = dat.ra_sexegesimal_to_decimal.ra_sexegesimal_to_decimal(ra2)
    if ':' in str(dec2):
        dec2 = dat.dec_sexegesimal_to_decimal.dec_sexegesimal_to_decimal(
            dec2)

    angularSeparation = None

    if ra1 and ra2 and dec1 and dec2:

        aa = (90.0 - dec1) * DEG_TO_RAD_FACTOR
        bb = (90.0 - dec2) * DEG_TO_RAD_FACTOR
        cc = (ra1 - ra2) * DEG_TO_RAD_FACTOR
        one = math.cos(aa) * math.cos(bb)
        two = math.sin(aa) * math.sin(bb) * math.cos(cc)

        # Because acos() returns NaN outside the ranges of -1 to +1
        # we need to check this.  Double precision decimal places
        # can give values like 1.0000000000002 which will throw an
        # exception.

        three = one + two
        if (three > 1.0):
            three = 1.0
        if (three < -1.0):
            three = -1.0

        angularSeparation = math.acos(three) * RAD_TO_DEG_FACTOR * 3600.0

    return angularSeparation

# LAST MODIFIED : April 15, 2013
# CREATED : April 15, 2013
# AUTHOR : DRYX


def convert_redshift_to_distance(z):
    """
    *Convert a redshift to various distance units*

    **Key Arguments:**
        - ``z`` -- the redshift to be converted

    **Return:**
        - ``results`` -- result dictionary including
            - ``dcmr_mpc`` -- co-moving radius distance
            - ``da_mpc`` -- angular distance
            - ``da_scale`` -- angular distance scale
            - ``dl_mpc`` -- luminosity distance (usually use this one)
            - ``dmod`` -- distance modulus (determined from luminosity distance)
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import math

    ################ >ACTION(S) ################
    # Cosmological Parameters (to be changed if required)
    WM = 0.3           # Omega_matter
    WV = 0.7           # Omega_vacuum
    H0 = 70.0           # Hubble constant (km s-1 Mpc-1)

    # Other variables
    h = H0 / 100.0
    WR = 4.165E-5 / (h * h)     # Omega_radiation
    WK = 1.0 - WM - WV - WR       # Omega_curvature = 1 - Omega(Total)
    c = 299792.458          # speed of light (km/s)

    # Arbitrarily set the values of these variables to zero just so we can
    # define them.
    DCMR = 0.0             # comoving radial distance in units of c/H0
    DCMR_Mpc = 0.0          # comoving radial distance in units of Mpc
    DA = 0.0                # angular size distance in units of c/H0
    DA_Mpc = 0.0            # angular size distance in units of Mpc
    # scale at angular size distance in units of Kpc / arcsec
    DA_scale = 0.0
    DL = 0.0                # luminosity distance in units of c/H0
    DL_Mpc = 0.0            # luminosity distance in units of Mpc
    # Distance modulus determined from luminosity distance
    DMOD = 0.0
    a = 0.0                 # 1/(1+z), the scale factor of the Universe

    az = 1.0 / (1.0 + z)        # 1/(1+z), for the given redshift

    # Compute the integral over a=1/(1+z) from az to 1 in n steps
    n = 1000
    for i in range(n):
        a = az + (1.0 - az) * (i + 0.5) / n
        adot = math.sqrt(WK + (WM / a) + (WR / (math.pow(a, 2)))
                         + (WV * math.pow(a, 2)))
        DCMR = DCMR + 1.0 / (a * adot)

    # comoving radial distance in units of c/H0
    DCMR = (1.0 - az) * DCMR / n
    # comoving radial distance in units of Mpc
    DCMR_Mpc = (c / H0) * DCMR

    # Tangental comoving radial distance
    x = math.sqrt(abs(WK)) * DCMR
    if x > 0.1:
        if WK > 0.0:
            ratio = 0.5 * (math.exp(x) - math.exp(-x)) / x
        else:
            ratio = math.sin(x) / x
    else:
        y = math.pow(x, 2)
        if WK < 0.0:
            y = -y
        ratio = 1 + y / 6.0 + math.pow(y, 2) / 120.0

    DA = az * ratio * DCMR  # angular size distance in units of c/H0
    DA_Mpc = (c / H0) * DA  # angular size distance in units of Mpc
    # scale at angular size distance in units of Kpc / arcsec
    DA_scale = DA_Mpc / 206.264806
    DL = DA / math.pow(az, 2)  # luminosity distance in units of c/H0
    DL_Mpc = (c / H0) * DL  # luminosity distance in units of Mpc
    # Distance modulus determined from luminosity distance
    DMOD = 5 * math.log10(DL_Mpc * 1e6) - 5

    results = \
        {
            "dcmr_mpc": DCMR_Mpc,
            "da_mpc": DA_Mpc,
            "da_scale": DA_scale,
            "dl_mpc": DL_Mpc,
            "dmod": DMOD,
            "z": z
        }

    return results


# LAST MODIFIED : April 15, 2013
# CREATED : April 15, 2013
# AUTHOR : DRYX
def convert_mpc_to_redshift(
        DL_Mpc):
    """
    *Convert a luminosity distance to a redshift*

    **Key Arguments:**
        - ``DL_Mpc`` -- luminosity distance (Mpc)

    **Return:**
        - ``redshift`` -- the calculated redshift
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import math
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    lowerLimit = 0.
    upperLimit = 30.
    redshift = upperLimit - lowerLimit
    distGuess = float(convert_redshift_to_distance(redshift)['dl_mpc'])

    distDiff = DL_Mpc - distGuess

    while math.fabs(distDiff) > 0.0001:
        if distGuess < DL_Mpc:
            lowerLimit = redshift
            redshift = lowerLimit + (upperLimit - lowerLimit) / 2.
            distGuess = float(convert_redshift_to_distance(redshift)['dl_mpc'])
        elif distGuess > DL_Mpc:
            upperLimit = redshift
            redshift = lowerLimit + (upperLimit - lowerLimit) / 2.
            distGuess = float(convert_redshift_to_distance(redshift)['dl_mpc'])
        distDiff = DL_Mpc - distGuess

    redshift = float("%5.4f" % (redshift,))

    return redshift


##########################################################################
# PRIVATE (HELPER) FUNCTIONS                                                                #
##########################################################################
if __name__ == '__main__':
    main()
