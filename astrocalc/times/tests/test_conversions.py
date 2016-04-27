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
    logLevel="DEBUG",
    options_first=False,
    projectName="astrocalc",
    tunnel=False
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

    def test_conversions_function(self):

        converter = conversions(
            log=log,
        )
        converter.ut_datetime_to_mjd(utDatetime="20160426t1446")

        converter.ut_datetime_to_mjd(utDatetime="20160426t144643")

        converter.ut_datetime_to_mjd(utDatetime="20160426t144643.033433")

        converter.ut_datetime_to_mjd(utDatetime="20161231t234643.033433")

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
