#!/usr/local/bin/python
# encoding: utf-8
"""
*Convert distances between measurement scales*

:Author:
    David Young

:Date Created:
    May 27, 2016
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import math
os.environ['TERM'] = 'vt100'
from fundamentals import tools


class converter():
    """
    *A converter to switch distance between various units of measurement*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary

    **Usage:**

        To instantiate a ``converter`` object:

        .. code-block:: python

            from astrocalc.distances import converter
            c = converter(log=log)

    """
    # Initialisation

    def __init__(
            self,
            log,
            settings=False,

    ):
        self.log = log
        log.debug("instansiating a new 'converter' object")
        self.settings = settings
        # xt-self-arg-tmpx

        # Initial Actions

        return None

    def distance_to_redshift(
            self,
            mpc):
        """*Convert a distance from MPC to redshift*

        The code works by iteratively converting a redshift to a distance, correcting itself and honing in on the true answer (within a certain precision)

        **Key Arguments:**
            - ``mpc`` -- distance in MPC (assumes a luminousity distance).

        **Return:**
            - ``redshift``

        .. todo::

            - replace convert_mpc_to_redshift in all code

        **Usage:**

            .. code-block:: python

                from astrocalc.distances import converter
                c = converter(log=log)
                z = c.distance_to_redshift(
                    mpc=500
                )

                print z

                # OUTPUT: 0.108
        """
        self.log.info('starting the ``distance_to_redshift`` method')

        lowerLimit = 0.
        upperLimit = 30.
        redshift = upperLimit - lowerLimit
        distGuess = float(self.redshift_to_distance(redshift)['dl_mpc'])

        distDiff = mpc - distGuess

        while math.fabs(distDiff) > 0.0001:
            if distGuess < mpc:
                lowerLimit = redshift
                redshift = lowerLimit + (upperLimit - lowerLimit) / 2.
                distGuess = float(
                    self.redshift_to_distance(redshift)['dl_mpc'])
            elif distGuess > mpc:
                upperLimit = redshift
                redshift = lowerLimit + (upperLimit - lowerLimit) / 2.
                distGuess = float(
                    self.redshift_to_distance(redshift)['dl_mpc'])
            distDiff = mpc - distGuess

        redshift = float("%5.4f" % (redshift,))

        self.log.info('completed the ``distance_to_redshift`` method')
        return redshift

    def redshift_to_distance(
            self,
            z,
            WM=0.3,
            WV=0.7,
            H0=70.0):
        """*convert redshift to various distance measurements*

        **Key Arguments:**
            - ``z`` -- redshift measurement.
            - ``WM`` -- Omega_matter. Default *0.3*
            - ``WV`` -- Omega_vacuum. Default *0.7*
            - ``H0`` -- Hubble constant. (km s-1 Mpc-1) Default *70.0*

        **Return:**
            - ``results`` -- result dictionary including
                - ``dcmr_mpc`` -- co-moving radius distance
                - ``da_mpc`` -- angular distance
                - ``da_scale`` -- angular distance scale
                - ``dl_mpc`` -- luminosity distance (usually use this one)
                - ``dmod`` -- distance modulus (determined from luminosity distance)

        ..  todo::

                - replace convert_redshift_to_distance in all other code

        **Usage:**

            .. code-block:: python

                from astrocalc.distances import converter
                c = converter(log=log)
                dists = c.redshift_to_distance(
                    z=0.343
                )

                print "Distance Modulus: " + str(dists["dmod"]) + " mag"
                print "Luminousity Distance: " + str(dists["dl_mpc"]) + " Mpc"
                print "Angular Size Scale: " + str(dists["da_scale"]) + " kpc/arcsec"
                print "Angular Size Distance: " + str(dists["da_mpc"]) + " Mpc"
                print "Comoving Radial Distance: " + str(dists["dcmr_mpc"]) + " Mpc"

                # OUTPUT :
                # Distance Modulus: 41.27 mag
                # Luminousity Distance: 1795.16 Mpc
                # Angular Size Scale: 4.85 kpc/arcsec
                # Angular Size Distance: 999.76 Mpc
                # Comoving Radial Distance: 1339.68 Mpc

                from astrocalc.distances import converter
                c = converter(log=log)
                dists = c.redshift_to_distance(
                    z=0.343,
                    WM=0.286,
                    WV=0.714,
                    H0=69.6
                )

                print "Distance Modulus: " + str(dists["dmod"]) + " mag"
                print "Luminousity Distance: " + str(dists["dl_mpc"]) + " Mpc"
                print "Angular Size Scale: " + str(dists["da_scale"]) + " kpc/arcsec"
                print "Angular Size Distance: " + str(dists["da_mpc"]) + " Mpc"
                print "Comoving Radial Distance: " + str(dists["dcmr_mpc"]) + " Mpc"

                # OUTPUT :
                # Distance Modulus: 41.29 mag
                # Luminousity Distance: 1811.71 Mpc
                # Angular Size Scale: 4.89 kpc/arcsec
                # Angular Size Distance: 1008.97 Mpc
                # Comoving Radial Distance: 1352.03 Mpc

        """
        self.log.info('starting the ``redshift_to_distance`` method')

        # VARIABLE
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

        # FIXING PRECISIONS
        # PRECISION TEST
        precision = len(repr(z).split(".")[-1])
        DCMR_Mpc = "%0.*f" % (precision, DCMR_Mpc)
        DA_Mpc = "%0.*f" % (precision, DA_Mpc)
        DA_scale = "%0.*f" % (precision, DA_scale)
        DL_Mpc = "%0.*f" % (precision, DL_Mpc)
        DMOD = "%0.*f" % (precision, DMOD)
        z = "%0.*f" % (precision, z)

        results = \
            {
                "dcmr_mpc": float(DCMR_Mpc),
                "da_mpc": float(DA_Mpc),
                "da_scale": float(DA_scale),
                "dl_mpc": float(DL_Mpc),
                "dmod": float(DMOD),
                "z": float(z)
            }

        self.log.info('completed the ``redshift_to_distance`` method')
        return results

    # use the tab-trigger below for new method
    # xt-class-method
