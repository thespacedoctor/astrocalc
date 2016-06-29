#!/usr/local/bin/python
# encoding: utf-8
"""
*Calculate separations between sky-coordinates*

:Author:
    David Young

:Date Created:
    April 21, 2016
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import math
os.environ['TERM'] = 'vt100'
from fundamentals import tools


class separations():
    """
    *The worker class for the separations module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary
        - ``ra1`` -- the right-ascension of the first location. Decimal degrees or sexegesimal.
        - ``dec1`` -- the declination of the first location. Decimal degrees or sexegesimal.
        - ``ra2`` -- the right-ascension of the second location. Decimal degrees or sexegesimal.
        - ``dec2`` -- the declination of the second location. Decimal degrees or sexegesimal.

    **Usage:**
        .. todo::

            - replace get_angular_separation throughout all code using dryxPython
            - replace getAngularSeparationthroughout all code using dryxPython

        You can input sexegesimal coordinates,

        .. code-block:: python

            from astrocalc.coords import separations
            calculator = separations(
                log=log,
                ra1="23:32:23.2324",
                dec1="-13:32:45.43553",
                ra2="23:32:34.642",
                dec2="-12:12:34.9334",
            )
            angularSeparation, north, east = calculator.get()
            print angularSeparation, north, east

            # OUT: '4813.39431', '4810.50214', '166.83941'

        or decimal degrees,

        .. code-block:: python

            from astrocalc.coords import separations
            calculator = separations(
                log=log,
                ra1=2.3342343,
                dec1=89.23244233,
                ra2=45.343545345,
                dec2=87.3435435
            )
            angularSeparation, north, east = calculator.get()
            print angularSeparation, north, east

            # OUT: '7774.4375', '-6800.0358', '4625.7620'

        or even a mix of both

        .. code-block:: python

            from astrocalc.coords import separations
            calculator = separations(
                log=log,
                ra1=352.5342343,
                dec1=89.23,
                ra2="23:32:34.642",
                dec2="89:12:34.9334"
            )
            angularSeparation, north, east = calculator.get()
            print angularSeparation, north, east

            # OUT: '78.9', '-73.1', '29.9')
    """
    # Initialisation

    def __init__(
            self,
            log,
            ra1,
            dec1,
            ra2,
            dec2,
            settings=False
    ):
        self.log = log
        log.debug("instansiating a new 'separations' object")
        self.settings = settings
        self.ra1 = ra1
        self.dec1 = dec1
        self.ra2 = ra2
        self.dec2 = dec2
        # xt-self-arg-tmpx
        return None

    def get(
            self):
        """*Calulate the angular separation between two locations on the sky*

        Input precision should be respected.

        **Key Arguments:**

        **Return:**
            - ``angularSeparation`` -- total angular separation between coordinates (arcsec)
            - ``north`` -- north-south separation between coordinates (arcsec)
            - ``east`` -- east-west separation between coordinates (arcsec)

        See main class usage for details.
        """
        self.log.info('starting the ``get_angular_separation`` method')

        from astrocalc.coords import unit_conversion

        # CONSTANTS
        pi = (4 * math.atan(1.0))
        DEG_TO_RAD_FACTOR = pi / 180.0
        RAD_TO_DEG_FACTOR = 180.0 / pi

        converter = unit_conversion(
            log=self.log
        )
        dec1 = converter.dec_sexegesimal_to_decimal(
            dec=self.dec1
        )
        dec2 = converter.dec_sexegesimal_to_decimal(
            dec=self.dec2
        )
        ra1 = converter.ra_sexegesimal_to_decimal(
            ra=self.ra1
        )
        ra2 = converter.ra_sexegesimal_to_decimal(
            ra=self.ra2
        )

        # PRECISION TEST
        precision = 100
        vals = [dec1, dec2, ra1, ra2]
        for v in vals:
            thisLen = len(repr(v * 3600.).split(".")[-1])
            if thisLen < precision:
                precision = thisLen

        angularSeparation = None

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

        # BE CAREFUL WITH PRECISION PROPAGATION
        thisVal = math.acos(three)
        angularSeparation = float(thisVal) * RAD_TO_DEG_FACTOR * 3600.0

        # Now work out N-S, E-W separations (object 1 relative to 2)
        north = -(dec1 - dec2) * 3600.0
        east = -(ra1 - ra2) * \
            math.cos((dec1 + dec2) * DEG_TO_RAD_FACTOR / 2.) * 3600.0

        angularSeparation = "%0.*f" % (precision, angularSeparation)
        north = "%0.*f" % (precision, north)
        east = "%0.*f" % (precision, east)

        self.log.info('completed the ``get_angular_separation`` method')
        return angularSeparation, north, east

    # use the tab-trigger below for new method
    # xt-class-method
