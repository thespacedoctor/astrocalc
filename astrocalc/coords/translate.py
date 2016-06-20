#!/usr/local/bin/python
# encoding: utf-8
"""
*Calculations to translate coordinates across the sky*

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
from astrocalc.coords import unit_conversion


class translate():
    """
    *Translate a set of coordinates north and east by distances given in arcsecs*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary. Default *False*
        - ``ra`` -- ra (decimal or sexegesimal)
        - ``dec`` -- dec (decimal or sexegesimal)
        - ``northArcsec`` -- number of arcsecs to move location to the north
        - ``eastArcsec`` -- number of arcsecs to move location to the east

    .. todo::

        - replace shift_coordinates class in all other code

    **Usage:**

        To shift a set of coordinates north and east by given distances:

        .. code-block:: python 

            # TRANSLATE COORDINATES ACROSS SKY
            from astrocalc.coords import translate
            ra, dec = translate(
                log=log,
                settings=settings,
                ra="14.546438",
                dec="-45.34232334",
                northArcsec=4560,
                eastArcsec=+967800
            ).get()  
    """
    # Initialisation

    def __init__(
            self,
            log,
            ra,
            dec,
            northArcsec,
            eastArcsec,
            settings=False,
    ):
        self.log = log
        log.debug("instansiating a new 'translate' object")
        self.settings = settings
        self.ra = ra
        self.dec = dec
        self.north = northArcsec / 3600.
        self.east = eastArcsec / 3600.
        # xt-self-arg-tmpx

        # CONSTANTS
        self.pi = (4 * math.atan(1.0))
        self.DEG_TO_RAD_FACTOR = self.pi / 180.0
        self.RAD_TO_DEG_FACTOR = 180.0 / self.pi

        # INITIAL ACTIONS
        # CONVERT RA AND DEC INTO DECIMAL DEGREES
        converter = unit_conversion(
            log=log
        )
        self.ra = converter.ra_sexegesimal_to_decimal(
            ra=self.ra
        )
        self.dec = converter.dec_sexegesimal_to_decimal(
            dec=self.dec
        )

        return None

    def get(self):
        """
        *translate the coordinates*

        **Return:**
            - ``ra`` -- the right-ascension of the translated coordinate
            - ``dec`` -- the declination of the translated coordinate
        """
        self.log.info('starting the ``get`` method')

        # PRECISION TEST
        decprecision = len(repr(self.dec).split(".")[-1])
        raprecision = len(repr(self.ra).split(".")[-1])

        dec2 = self.dec + self.north

        ra2 = self.ra + \
            ((self.east) /
             (math.cos((self.dec + dec2) * self.DEG_TO_RAD_FACTOR / 2.)))

        # FIX VALUES THAT CROSS RA/DEC LIMITS
        while ra2 > 360. or ra2 < 0.:
            while ra2 > 360.:
                ra2 = ra2 - 360.
            while ra2 < 0.:
                ra2 = ra2 + 360.
        while dec2 > 90. or dec2 < -90.:
            while dec2 > 90.:
                dec2 = 180. - dec2
            while dec2 < -90.:
                dec2 = -180. - dec2

        ra2 = "%0.*f" % (raprecision, ra2)
        dec2 = "%0.*f" % (decprecision, dec2)

        self.log.info('completed the ``get`` method')
        return ra2, dec2

    # xt-class-method
