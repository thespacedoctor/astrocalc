#!/usr/local/bin/python
# encoding: utf-8
"""
*Convert times between various epochs and units*

:Author:
    David Young

:Date Created:
    April 21, 2016
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
from fundamentals import tools


class conversions():
    """
    *The worker class for the conversions module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary

    **Usage:**
        .. todo::

            - add usage info
            - create a sublime snippet for usage
            - add mjd_to_date
            - add decimal_day_to_day_hour_min_sec
            - add date_to_mjd
            - convert all functions in __init__ to modules

        .. code-block:: python 

            usage code   
    """
    # Initialisation

    def __init__(
            self,
            log,
            settings=False,
    ):
        self.log = log
        log.debug("instansiating a new 'conversions' object")
        self.settings = settings
        # xt-self-arg-tmpx

        return None

    def get(self):
        """
        *get the conversions object*

        **Return:**
            - ``conversions``

        .. todo::

            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        conversions = None

        self.log.info('completed the ``get`` method')
        return conversions

    def ut_datetime_to_mjd(
            self,
            utDatetime):
        """*ut datetime to mjd*

        If the date given has no time associated with it (e.g. ``20160426``), then the datetime assumed is ``20160426 00:00:00.0``.

        Precision should be respected. 

        **Key Arguments:**
            - ``utDatetime`` -- UT datetime. Can accept various formats e.g. ``201604261444``, ``20160426``, ``20160426144444.5452``, ``2016-04-26 14:44:44.234``, ``20160426 14h44m44.432s`` 

        **Return:**
            - ``mjd`` -- the MJD

        **Usage:**

            .. code-block:: python 

                from astrocalc.times import conversions
                converter = conversions(
                    log=log
                )
                mjd = converter.ut_datetime_to_mjd(utDatetime="20160426t1446")
                print mjd

                # OUT: 57504.6153

                mjd = converter.ut_datetime_to_mjd(utDatetime="2016-04-26 14:44:44.234")
                print mjd

                # OUT: 57504.61440
        """
        self.log.info('starting the ``ut_datetime_to_mjd`` method')

        import time
        import re
        mjd = None

        # TRIM WHITESPACE FROM AROUND STRING
        utDatetime = utDatetime.strip()

        # DATETIME REGEX
        matchObject = re.match(
            r'^(?P<year>\d{4})\D?(?P<month>(0\d|1[0-2]))\D?(?P<day>([0-2]\d|3[0-1])(\.\d+)?)(\D?(?P<hours>([0-1]\d|2[0-3]))\D?(?P<minutes>\d{2})(\D?(?P<seconds>\d{2}(\.\d*?)?))?)?s?$', utDatetime)

        # RETURN ERROR IF REGEX NOT MATCHED
        if not matchObject:
            self.log.error(
                'UT Datetime is not in a recognised format. Input value was `%(utDatetime)s`' % locals())
            raise IOError(
                'UT Datetime is not in a recognised format. Input value was `%(utDatetime)s`' % locals())

        year = matchObject.group("year")
        month = matchObject.group("month")
        day = matchObject.group("day")
        hours = matchObject.group("hours")
        minutes = matchObject.group("minutes")
        seconds = matchObject.group("seconds")

        # CLEAN NUMBERS AND SET OUTPUT PRECISION
        if "." in day:
            fhours = (float(day) - int(float(day))) * 24
            hours = int(fhours)
            fminutes = (fhours - hours) * 60
            minutes = int(fminutes)
            seconds = fhours - minutes
            precision = len(repr(day).split(".")[-1])
        elif not hours:
            hours = "00"
            minutes = "00"
            seconds = "00"
            precision = 1
        elif not seconds:
            seconds = "00"
            # PRECISION TO NEAREST MIN i.e. 0.000694444 DAYS
            precision = 4
        else:
            if "." not in seconds:
                precision = 5
            else:
                decLen = len(seconds.split(".")[-1])
                precision = 5 + decLen

        # CONVERT VALUES TO FLOAT
        seconds = float(seconds)
        year = float(year)
        month = float(month)
        day = float(day)
        hours = float(hours)
        minutes = float(minutes)

        # DETERMINE EXTRA TIME (SMALLER THAN A SEC)
        extraTime = 0.
        if "." in repr(seconds):
            extraTime = float("." + repr(seconds).split(".")
                              [-1]) / (24. * 60. * 60.)

        # CONVERT TO UNIXTIME THEN MJD
        t = (int(year), int(month), int(day), int(hours),
             int(minutes), int(seconds), 0, 0, 0)
        unixtime = int(time.mktime(t))
        mjd = (unixtime / 86400.0 - 2400000.5 + 2440587.5) + extraTime

        mjd = "%0.*f" % (precision, mjd)

        self.log.info('completed the ``ut_datetime_to_mjd`` method')
        return mjd

    def mjd_to_ut_datetime(
            self,
            mjd):
        """*mjd to ut datetime*

        Precision should be respected. 

        **Key Arguments:**
            - ``mjd`` -- time in MJD.

        **Return:**
            - ``utDatetime`` - the UT datetime in string format

        **Usage:**

            .. code-block:: python 

                from astrocalc.times import conversions
                converter = conversions(
                    log=log
                )
                utDate = converter.mjd_to_ut_datetime(mjd=57504.61577585013)
                print utDate

                # OUT: 2016-04-26 14:46:43.033
        """
        self.log.info('starting the ``mjd_to_ut_datetime`` method')

        from datetime import datetime

        # CONVERT TO UNIXTIME
        unixtime = (float(mjd) + 2400000.5 - 2440587.5) * 86400.0
        theDate = datetime.utcfromtimestamp(unixtime)

        # DETERMINE PRECISION
        strmjd = repr(mjd)
        if "." not in strmjd:
            precisionUnit = "day"
            precision = 0
            utDatetime = theDate.strftime("%Y-%m-%d")
        else:
            lenDec = len(strmjd.split(".")[-1])
            if lenDec < 2:
                precisionUnit = "day"
                precision = 0
                utDatetime = theDate.strftime("%Y-%m-%d")
            elif lenDec < 3:
                precisionUnit = "hour"
                precision = 0
                utDatetime = theDate.strftime("%Y-%m-%d")
            elif lenDec < 5:
                precisionUnit = "minute"
                precision = 0
                utDatetime = theDate.strftime("%Y-%m-%d %H:%M")
            else:
                precisionUnit = "second"
                precision = lenDec - 5
                if precision > 3:
                    precision = 3
                secs = float(theDate.strftime("%S.%f"))
                secs = "%02.*f" % (precision, secs)
                utDatetime = theDate.strftime("%Y-%m-%d %H:%M:") + secs

        self.log.info('completed the ``mjd_to_ut_datetime`` method')
        return utDatetime

    # use the tab-trigger below for new method
    # xt-class-method
