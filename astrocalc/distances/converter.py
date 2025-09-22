#!/usr/local/bin/python
# encoding: utf-8
"""
*Convert distances between measurement scales*

Author
: David Young
"""
from __future__ import division
from builtins import range
from builtins import object
from past.utils import old_div
import sys
import os
import math
os.environ['TERM'] = 'vt100'


class converter(object):
    """
    *A converter to switch distance between various units of measurement*

    **Key Arguments**

    - ``log`` -- logger
    - ``settings`` -- the settings dictionary


    **Usage**

    To instantiate a ``converter`` object:

    ```python
    from astrocalc.distances import converter
    c = converter(log=log)
    ```

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

        **Key Arguments**

        - ``mpc`` -- distance in MPC (assumes a luminousity distance).


        **Return**

        - ``redshift``


        .. todo::

            - replace convert_mpc_to_redshift in all code

        **Usage**

        ```python
        from astrocalc.distances import converter
        c = converter(log=log)
        z = c.distance_to_redshift(
            mpc=500
        )

        print(z)

        # OUTPUT: 0.108
        ```

        """
        self.log.debug('starting the ``distance_to_redshift`` method')

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

        self.log.debug('completed the ``distance_to_redshift`` method')
        return redshift

    def redshift_to_distance(
            self,
            z,
            WM=0.3,
            WV=0.7,
            H0=70.0):
        """*convert redshift to various distance measurements*

        **Key Arguments**

        - ``z`` -- redshift measurement.
        - ``WM`` -- Omega_matter. Default *0.3*
        - ``WV`` -- Omega_vacuum. Default *0.7*
        - ``H0`` -- Hubble constant. (km s-1 Mpc-1) Default *70.0*


        **Return**

        - ``results`` -- result dictionary including
        - ``dcmr_mpc`` -- co-moving radius distance
        - ``da_mpc`` -- angular distance
        - ``da_scale`` -- angular distance scale
        - ``dl_mpc`` -- luminosity distance (usually use this one)
        - ``dmod`` -- distance modulus (determined from luminosity distance)


        ..  todo::

                - replace convert_redshift_to_distance in all other code

        **Usage**

        ```python
        from astrocalc.distances import converter
        c = converter(log=log)
        dists = c.redshift_to_distance(
            z=0.343
        )

        print("Distance Modulus: " + str(dists["dmod"]) + " mag")
        print("Luminousity Distance: " + str(dists["dl_mpc"]) + " Mpc")
        print("Angular Size Scale: " + str(dists["da_scale"]) + " kpc/arcsec")
        print("Angular Size Distance: " + str(dists["da_mpc"]) + " Mpc")
        print("Comoving Radial Distance: " + str(dists["dcmr_mpc"]) + " Mpc")

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

        print("Distance Modulus: " + str(dists["dmod"]) + " mag")
        print("Luminousity Distance: " + str(dists["dl_mpc"]) + " Mpc")
        print("Angular Size Scale: " + str(dists["da_scale"]) + " kpc/arcsec")
        print("Angular Size Distance: " + str(dists["da_mpc"]) + " Mpc")
        print("Comoving Radial Distance: " + str(dists["dcmr_mpc"]) + " Mpc")

        # OUTPUT :
        # Distance Modulus: 41.29 mag
        # Luminousity Distance: 1811.71 Mpc
        # Angular Size Scale: 4.89 kpc/arcsec
        # Angular Size Distance: 1008.97 Mpc
        # Comoving Radial Distance: 1352.03 Mpc
        ```

        """
        self.log.debug('starting the ``redshift_to_distance`` method')

        from scipy.integrate import quad

        # VARIABLE
        h = H0 / 100.0
        WR = 4.165E-5/(h * h)     # Omega_radiation
        WK = 1.0 - WM - WV - WR       # Omega_curvature = 1 - Omega(Total)
        c = 299792.458          # speed of light (km/s)
        factor = c / H0  # Precompute conversion factor

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

        # Compute the integral over a=1/(1+z) from az to 1 using scipy.integrate.quad
        def integrand(a):
            adot = math.sqrt(WK + (WM / a) + (WR / (a ** 2)) + (WV * a ** 2))
            return 1.0 / (a * adot)

        DCMR, _ = quad(integrand, az, 1.0, epsabs=1e-10, epsrel=1e-10)
        # comoving radial distance in units of Mpc
        DCMR_Mpc = (factor) * DCMR

        # Tangential comoving radial distance (optimized)
        x = math.sqrt(abs(WK)) * DCMR
        if x > 0.1:
            if WK > 0.0:
                ratio = math.sinh(x) / x
            else:
                ratio = math.sin(x) / x
        else:
            y = x * x
            if WK < 0.0:
                y = -y
            ratio = 1 + y / 6.0 + y * y / 120.0

        DA = az * ratio * DCMR  # angular size distance in units of c/H0
        DA_Mpc = factor * DA  # angular size distance in units of Mpc
        # scale at angular size distance in units of Kpc / arcsec
        DA_scale = DA_Mpc / 206.264806
        # luminosity distance in units of c/H0
        DL = DA / (az ** 2)
        DL_Mpc = factor * DL  # luminosity distance in units of Mpc
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

        self.log.debug('completed the ``redshift_to_distance`` method')
        return results

    # use the tab-trigger below for new method
    # xt-class-method
