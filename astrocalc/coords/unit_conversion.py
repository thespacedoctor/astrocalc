#!/usr/local/bin/python
# encoding: utf-8
"""
*Convert coordinates from decimal to sexagesimal units and vice-versa*

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


class unit_conversion():
    """
    *The worker class for the unit_conversion module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary (prob not required)

    **Usage:**
        .. todo::

            - add usage info
            - create a sublime snippet for usage
            - add ra_sexegesimal_to_decimal

        .. code-block:: python

            usage code

    .. todo::

        - @review: when complete, clean unit_conversion class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
            self,
            log,
            settings=False
    ):
        self.log = log
        log.debug("instansiating a new 'unit_conversion' object")
        self.settings = settings
        # xt-self-arg-tmpx

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions

        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """
        *get the unit_conversion object*

        **Return:**
            - ``unit_conversion``

        .. todo::

            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        unit_conversion = None

        self.log.info('completed the ``get`` method')
        return unit_conversion

    def dec_sexegesimal_to_decimal(
            self,
            dec):
        """
        *Convert a declination from sexegesimal format to decimal degrees.*

        Precision should be respected. If a float is passed to this method, the same float will be returned (useful if unclear which format coordinates are in).

        The code will attempt to read the sexegesimal value in whatever form it is passed. Any of the following should be handled correctly:

        - ``+1:58:05.45341``
        - ``01:5:05``
        - ``+1 58 05.45341``
        - ``-23h53m05s``

        **Key Arguments:**
            - ``dec`` - DEC in sexegesimal format.

        **Return:**
            - ``decDeg`` -- declination converted to decimal degrees

        **Usage:**

            .. todo::

                - replace dryxPython declination_sexegesimal_to_decimal with this version in all my code
                - replace coords_sex_to_dec in all code

            .. code-block:: python

                from astrocalc.coords import unit_conversion
                converter = unit_conversion(
                    log=log
                )
                dec = converter.dec_sexegesimal_to_decimal(
                    dec="-23:45:21.23232"
                )
                print dec

                # OUTPUT: -23.7558978667
        """
        self.log.info(
            'starting the ``dec_sexegesimal_to_decimal`` method')

        import re

        # TEST TO SEE IF DECIMAL DEGREES PASSED
        try:
            dec = float(dec)
            if dec > -90. and dec < 90.:
                self.log.info(
                    'declination seems to already be in decimal degrees, returning original value' % locals())
                return float(dec)
        except:
            pass

        # REMOVE SURROUNDING WHITESPACE
        dec = str(dec).strip()

        # LOOK FOR A MINUS SIGN.  NOTE THAT -00 IS THE SAME AS 00.
        regex = re.compile(
            '^([\+\-]?(\d|[0-8]\d))\D+([0-5]\d)\D+([0-6]?\d(\.\d+)?)$')
        decMatch = regex.match(dec)

        if decMatch:
            degrees = decMatch.group(1)
            minutes = decMatch.group(3)
            seconds = decMatch.group(4)

            if degrees[0] == '-':
                sgn = -1
            else:
                sgn = 1

            degrees = abs(float(degrees))
            minutes = float(minutes)
            seconds = float(seconds)

            # PRECISION TEST
            # 1s = .000277778 DEGREE
            # THEREFORE REPORT SECONDS TO A PRECISION = INPUT PRECISION + 4
            decimalLen = len(repr(seconds).split(".")[-1])
            precision = decimalLen + 4

            decDeg = (degrees + (minutes / 60.0)
                              + (seconds / 3600.0)) * sgn

            decDeg = "%0.*f" % (precision, decDeg)

        else:
            raise IOError(
                "could not convert dec to decimal degrees, could not parse sexegesimal input. Original value was `%(dec)s`" % locals())

        decDeg = float(decDeg)
        self.log.debug('decDeg: %(decDeg)s' % locals())
        self.log.info(
            'completed the ``dec_sexegesimal_to_decimal`` method')

        return float(decDeg)

    def ra_sexegesimal_to_decimal(
        self,
        ra
    ):
        """
        *Convert a right-ascension from sexegesimal format to decimal degrees.*

        Precision should be respected. If a float is passed to this method, the same float will be returned (useful if unclear which format coordinates are in).

        The code will attempt to read the sexegesimal value in whatever form it is passed. Any of the following should be handled correctly

        - ``23:45:21.23232``
        - ``23h45m21.23232s``
        - ``23 45 21.23232``
        - ``2 04 21.23232``
        - ``04:45  21``

        **Key Arguments:**
            - ``ra`` -- ra in sexegesimal units

        **Return:**
            - ``decimalDegrees``

        **Usage:**

            .. code-block:: python

                - replace dryxPython ra_sexegesimal_to_decimal with this version in all my code

                from astrocalc.coords import unit_conversion
                converter = unit_conversion(
                    log=log
                )
                ra = converter.ra_sexegesimal_to_decimal(
                    ra="04:45  21"
                )
                print ra

                # OUTPUT: 71.3375
        """
        import re

        # TEST TO SEE IF DECIMAL DEGREES PASSED
        try:
            ra = float(ra)
            if ra >= 0. and ra <= 360.:
                self.log.info(
                    'RA seems to already be in decimal degrees, returning original value' % locals())
                return float(ra)
        except:
            pass

        # REMOVE SURROUNDING WHITESPACE
        ra = str(ra).strip()

        regex = re.compile(
            '^(\+?(\d|[0-1]\d|2[0-3]))\D+([0-5]\d)\D+([0-6]?\d(\.\d*?)?)(s)?\s*?$')
        raMatch = regex.match(ra)

        if raMatch:
            degrees = raMatch.group(1)
            minutes = raMatch.group(3)
            seconds = raMatch.group(4)

            degrees = abs(float(degrees)) * 15.0
            minutes = float(minutes) * 15.0
            seconds = float(seconds) * 15.0

            # PRECISION TEST
            # 1s ARCSEC = .000018519 DEGREE
            # THEREFORE REPORT SECONDS TO A PRECISION = INPUT PRECISION + 5
            decimalLen = len(repr(seconds).split(".")[-1])
            precision = decimalLen + 5

            decimalDegrees = (degrees + (minutes / 60.0)
                              + (seconds / 3600.0))

            decimalDegrees = "%0.*f" % (precision, decimalDegrees)

        else:
            raise IOError(
                "could not convert ra to decimal degrees, could not parse sexegesimal input. Original value was `%(ra)s`" % locals())

        raDeg = decimalDegrees
        self.log.debug('raDeg: %(decimalDegrees)s' % locals())
        self.log.info(
            'completed the ``ra_sexegesimal_to_decimal`` method')

        return float(raDeg)

    def ra_decimal_to_sexegesimal(
            self,
            ra,
            delimiter=":"):
        """
        *Convert a right-ascension between decimal degrees and sexegesimal.*

        Precision should be respected.

        **Key Arguments:**
            - ``ra`` -- RA in decimal degrees. Will try and convert to float before performing calculation.
            - ``delimiter`` -- how to delimit the RA units. Default *:*

        **Return:**
            - ``sexegesimal`` -- ra in sexegesimal units

        **Usage:**
            ..  todo::

                - replace ra_to_sex from dryxPython in all code

            .. code-block:: python 

                from astrocalc.coords import unit_conversion
                converter = unit_conversion(
                    log=log
                )
                ra = converter.ra_decimal_to_sexegesimal(
                    ra="-23.454676456",
                    delimiter=":"
                )
                print ra

                # OUT: 22:26:10.87
        """
        self.log.info('starting the ``ra_decimal_to_sexegesimal`` method')

        # CONVERT RA TO FLOAT
        try:
            self.log.debug("attempting to convert RA to float")
            ra = float(ra)
        except Exception, e:
            self.log.error(
                "could not convert RA to float - failed with this error: %s " % (str(e),))
            return -1

        # COMPLAIN IF RA NOT BETWEEN -360 - 360
        if ra > 0. and ra < 360.:
            pass
        elif ra < 0 and ra > -360.:
            ra = 360. + ra
        else:
            self.log.error(
                "RA must be between 0 - 360 degrees")
            return -1

        # PRECISION TEST
        # 1s ARCSEC = .000018519 DEGREE
        # THEREFORE REPORT SECONDS TO A PRECISION = INPUT PRECISION - 5
        decimalLen = len(repr(ra).split(".")[-1])
        precision = decimalLen - 5

        # CALCULATION FROM DECIMAL DEGREES
        import math
        ra_hh = int(ra / 15)
        ra_mm = int((ra / 15 - ra_hh) * 60)
        ra_ss = int(((ra / 15 - ra_hh) * 60 - ra_mm) * 60)
        ra_ff = ((ra / 15 - ra_hh) * 60 - ra_mm) * 60 - ra_ss

        # SET PRECISION
        ra_ff = repr(ra_ff)[2:]
        ra_ff = ra_ff[:precision]
        if len(ra_ff):
            ra_ff = "." + ra_ff
        if precision < 0:
            ra_ff = ""

        sexegesimal = '%02d' % ra_hh + delimiter + '%02d' % ra_mm + \
            delimiter + '%02d' % ra_ss + ra_ff

        self.log.info('completed the ``ra_decimal_to_sexegesimal`` method')
        return sexegesimal

    def dec_decimal_to_sexegesimal(
            self,
            dec,
            delimiter=":"):
        """
        *Convert a declination between decimal degrees and sexegesimal.*

        Precision should be respected.

        **Key Arguments:**
            - ``dec`` -- DEC in decimal degrees. Will try and convert to float before performing calculation.
            - ``delimiter`` -- how to delimit the RA units. Default *:*

        **Return:**
            - ``sexegesimal`` -- ra in sexegesimal units

        **Usage:**
            ..  todo::

                - replace dec_to_sex in dryxPython in all code

            .. code-block:: python 

                from astrocalc.coords import unit_conversion
                converter = unit_conversion(
                    log=log
                )
                dec = converter.dec_decimal_to_sexegesimal(
                    dec="-3.454676456",
                    delimiter=":"
                )
                print dec

                # OUT: -03:27:16.8
        """
        self.log.info('starting the ``dec_decimal_to_sexegesimal`` method')

        import math

        # CONVERT DEC TO FLOAT
        try:
            self.log.debug("attempting to convert RA to float")
            dec = float(dec)
        except Exception, e:
            self.log.error(
                "could not convert RA to float - failed with this error: %s " % (str(e),))
            return -1

        # COMPLAIN IF DEC NOT BETWEEN -90 - 90
        if dec > -90. and dec < 90.:
            pass
        else:
            self.log.error(
                "DEC must be between -90 - 90 degrees")
            return -1

        if (dec >= 0):
            hemisphere = '+'
        else:
            hemisphere = '-'
            dec *= -1

        # PRECISION TEST
        # 1s = .000277778 DEGREE
        # THEREFORE REPORT SECONDS TO A PRECISION = INPUT PRECISION - 4
        decimalLen = len(repr(dec).split(".")[-1])
        precision = decimalLen - 4

        dec_deg = int(dec)
        dec_mm = int((dec - dec_deg) * 60)
        dec_ss = int(((dec - dec_deg) * 60 - dec_mm) * 60)
        dec_f = (((dec - dec_deg) * 60 - dec_mm) * 60) - dec_ss

        # SET PRECISION
        dec_f = repr(dec_f)[2:]
        dec_f = dec_f[:precision]
        if len(dec_f):
            dec_f = "." + dec_f
        if precision < 0:
            dec_f = ""

        sexegesimal = hemisphere + '%02d' % dec_deg + delimiter + \
            '%02d' % dec_mm + delimiter + '%02d' % dec_ss + dec_f

        self.log.info('completed the ``dec_decimal_to_sexegesimal`` method')
        return sexegesimal

    # use the tab-trigger below for new method
    def ra_dec_to_cartesian(
            self,
            ra,
            dec):
        """*Convert an RA, DEC coordinate set to x, y, z cartesian coordinates*

        **Key Arguments:**
            - ``ra`` -- right ascension in sexegesimal or decimal degress.
            - ``dec`` -- declination in sexegesimal or decimal degress.

        **Return:**
            - ``cartesians`` -- tuple of (x, y, z) coordinates

        ..  todo::

            - replace calculate_cartesians in all code

        **Usage:**

            .. code-block:: python 

                from astrocalc.coords import unit_conversion
                converter = unit_conversion(
                    log=log
                )
                x, y, z = converter.ra_dec_to_cartesian(
                    ra="23 45 21.23232",
                    dec="+01:58:5.45341"
                )
                print x, y, z

                # OUTPUT: 0.9973699780687104, -0.06382462462791459, 0.034344492110465606
        """
        self.log.info('starting the ``ra_dec_to_cartesian`` method')

        ra = self.ra_sexegesimal_to_decimal(
            ra=ra
        )
        dec = self.dec_sexegesimal_to_decimal(
            dec=dec
        )

        ra = math.radians(ra)
        dec = math.radians(dec)
        cos_dec = math.cos(dec)
        cx = math.cos(ra) * cos_dec
        cy = math.sin(ra) * cos_dec
        cz = math.sin(dec)

        cartesians = (cx, cy, cz)

        self.log.info('completed the ``ra_dec_to_cartesian`` method')
        return cartesians

    # use the tab-trigger below for new method
    # xt-class-method
