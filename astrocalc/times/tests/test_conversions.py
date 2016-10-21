import os
import nose
import shutil
import yaml
from astrocalc.times import conversions
from astrocalc.utKit import utKit

from fundamentals import tools

su = tools(
    arguments={"settingsFile": None},
    docString=__doc__,
    logLevel="WARNING",
    options_first=False,
    projectName="astrocalc"
)
arguments, settings, log, dbConn = su.setup()

# load settings
stream = file(
    "/Users/Dave/.config/astrocalc/astrocalc.yaml", 'r')
settings = yaml.load(stream)
stream.close()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()


class test_conversions():

    def test_utdatetime_conversions_function(self):

        converter = conversions(
            log=log,
        )

        print "\nUT = 20160426t144643.033433"
        print converter.ut_datetime_to_mjd(utDatetime="20160426t144643.033433")
        print converter.mjd_to_ut_datetime(mjd=57504.61577585013)

        print "\nUT = 20160426t144643.033433"
        print converter.ut_datetime_to_mjd(utDatetime="20160426t144643.033433")
        print converter.mjd_to_ut_datetime(mjd=57504.61577585013)

        print "\nUT = 20160426t144643.033433"
        print converter.ut_datetime_to_mjd(utDatetime="20160426t144643.033433")
        print converter.mjd_to_ut_datetime(mjd=57504.61577585013)

        print "\nUT = 20160426t1446"
        print converter.ut_datetime_to_mjd(utDatetime="20160426t1446")
        print converter.mjd_to_ut_datetime(mjd=57504.6153)
        print "\nUT = 20160426t144643"
        print converter.ut_datetime_to_mjd(utDatetime="20160426t144643")
        print converter.mjd_to_ut_datetime(mjd=57504.61578)
        print "\nUT = 20160426t144643.033433"
        print converter.ut_datetime_to_mjd(utDatetime="20160426t144643.033433")
        print converter.mjd_to_ut_datetime(mjd=57504.61577585013)
        print "\nUT = 20161231t234643.033433"
        print converter.ut_datetime_to_mjd(utDatetime="20161231t234643.033433")
        print converter.ut_datetime_to_mjd(utDatetime="20161231t234643.033433")
        print converter.mjd_to_ut_datetime(mjd="57753.99077585013")
        print "\nUT = 201604261444"
        print converter.ut_datetime_to_mjd(utDatetime="201604261444")
        print converter.mjd_to_ut_datetime(mjd=57504.6139)
        print "\nUT = 20160426"
        print converter.ut_datetime_to_mjd(utDatetime="20160426")
        print converter.mjd_to_ut_datetime(mjd=57504.0)
        print "\nUT = 2016-04-26.33433"
        print converter.ut_datetime_to_mjd(utDatetime="2016-04-26.33433")
        print converter.mjd_to_ut_datetime(mjd=57504.33411)
        print "\nUT = 20160426144444.5452"
        print converter.ut_datetime_to_mjd(utDatetime="20160426144444.5452")
        print converter.mjd_to_ut_datetime(mjd=57504.614404459)
        print "\nUT = 2016-04-26 14:44:44.234"
        print converter.ut_datetime_to_mjd(utDatetime="2016-04-26 14:44:44.234")
        print converter.mjd_to_ut_datetime(mjd=57504.61440086)
        print "\nUT = 20160426 14h44m44.432s"
        print converter.ut_datetime_to_mjd(utDatetime="20160426 14h44m44.432s")
        print converter.mjd_to_ut_datetime(mjd=57504.61440315)
        print "\nUT = 2016-04-26T14:44:44.234"
        print converter.ut_datetime_to_mjd(utDatetime="2016-04-26T14:44:44.234")
        print converter.mjd_to_ut_datetime(
            mjd=57504.61440086,
            sqlDate=True
        )

    def test_mjd_conversions_function(self):

        converter = conversions(
            log=log,
        )
        print converter.mjd_to_ut_datetime(mjd=57504.61440)
        print converter.mjd_to_ut_datetime(mjd=57504.61440)
        print converter.mjd_to_ut_datetime(mjd=57504.61440)
        print converter.mjd_to_ut_datetime(mjd=57504.61440)
        print converter.mjd_to_ut_datetime(mjd=57504.61440)
        print converter.mjd_to_ut_datetime(mjd=57504.61440)
        print converter.mjd_to_ut_datetime(mjd=57504.61440)
        print converter.mjd_to_ut_datetime(mjd=57504.61440)
        print converter.mjd_to_ut_datetime(mjd=57504.61440)
        print converter.mjd_to_ut_datetime(mjd=57504.61440)

    def test_decimal_day_to_day_hour_min_sec_function(self):

        converter = conversions(
            log=log,
        )
        daysInt, hoursInt, minsInt, secFloat = converter.decimal_day_to_day_hour_min_sec(
            daysFloat=24.2453)
        print "%(daysInt)s days, %(hoursInt)s hours, %(minsInt)s mins, %(secFloat)s sec" % locals()

        daysInt, hoursInt, minsInt, secFloat = converter.decimal_day_to_day_hour_min_sec(
            daysFloat=24.12345)
        print "%(daysInt)s days, %(hoursInt)s hours, %(minsInt)s mins, %(secFloat)s sec" % locals()

        daysInt, hoursInt, minsInt, secFloat = converter.decimal_day_to_day_hour_min_sec(
            daysFloat=24.2)
        print "%(daysInt)s days, %(hoursInt)s hours, %(minsInt)s mins, %(secFloat)s sec" % locals()

        daysInt, hoursInt, minsInt, secFloat = converter.decimal_day_to_day_hour_min_sec(
            daysFloat=24.1232435454)
        print "%(daysInt)s days, %(hoursInt)s hours, %(minsInt)s mins, %(secFloat)s sec" % locals()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
