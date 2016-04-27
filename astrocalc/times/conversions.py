#!/usr/local/bin/python
# encoding: utf-8
"""
*Convert times between various epochs and units*

:Author:
    David Young

:Date Created:
    April 21, 2016

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython
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

    .. todo::

        - @review: when complete, clean conversions class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
            self,
            log,
            settings=False,

    ):
        self.log = log
        log.debug("instansiating a new 'conversions' object")
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

        If the date given has no time (e.g. ``20160426``), then the datetime assumed is ``20160426 00:00:00.0``

        **Key Arguments:**
            - ``utDatetime`` -- UT datetime in format "20160426t1444"


        **Return:**
            - None

        **Usage:**
            ..  todo::

                add usage info
                create a sublime snippet for usage

            .. code-block:: python 

                usage code 

        .. todo::

            - @review: when complete, clean methodName method
            - @review: when complete add logging
        """
        self.log.info('starting the ``ut_datetime_to_mjd`` method')

        import time
        import re
        mjd = None

        # TRIM WHITESPACE FROM AROUND STRING
        utDatetime = utDatetime.strip()

        matchObject = re.match(
            r'^(?P<year>\d{4})\D?(?P<month>(0\d|1[0-2]))\D?(?P<day>([0-2]\d|3[0-1]))(\D?(?P<hours>([0-1]\d|2[0-3]))\D?(?P<minutes>\d{2})(\D?(?P<seconds>\d{2}(\.\d*?)?))?)?$', utDatetime)

        if not matchObject:
            self.log.error(
                'UT Datetime is not in a recognised format. Input value was `%(utDatetime)s`' % locals())
            sys.exit(0)

        year = matchObject.group("year")
        month = matchObject.group("month")
        day = matchObject.group("day")
        hours = matchObject.group("hours")
        minutes = matchObject.group("minutes")
        seconds = matchObject.group("seconds")

        if not hours:
            hours = "00"
            minutes = "00"
            seconds = "00"
            precision = 1
        elif not seconds:
            seconds = "00"
            # PRECISION TO NEAREST MIN i.e. 0.000694444 DAYS
            precision = 4

        print "datetime", utDatetime
        print "year", year
        print "month", month
        print "day", day
        print "hours", hours
        print "minutes", minutes
        print "seconds", seconds

        return

        if not len(hours):
            hours = 0
        if not len(minutes):
            minutes = 0
        if not len(seconds):
            seconds = 0

        t = (int(year), int(month), int(day), int(hours),
             int(minutes), int(seconds), 0, 0, 0)
        unixtime = int(time.mktime(t))
        mjd = unixtime / 86400.0 - 2400000.5 + 2440587.5

        self.log.info('completed the ``ut_datetime_to_mjd`` method')
        return None

    # use the tab-trigger below for new method
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
