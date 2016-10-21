import os
import nose
import shutil
import yaml
from astrocalc.utKit import utKit

from fundamentals import tools

su = tools(
    arguments={"settingsFile": None},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName="astrocalc"
)
arguments, settings, log, dbConn = su.setup()

# # load settings
# stream = file(
#     "/Users/Dave/.config/astrocalc/astrocalc.yaml", 'r')
# settings = yaml.load(stream)
# stream.close()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# load settings
stream = file(
    pathToInputDir + "/example_settings.yaml", 'r')
settings = yaml.load(stream)
stream.close()

import shutil
try:
    shutil.rmtree(pathToOutputDir)
except:
    pass

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)

# xt-setup-unit-testing-files-and-folders


class test_coordinates_to_array():

    def test_coordinates_to_array(self):

        raList = ["13:20:00.00", 200.0, "13:20:00.00", 175.23, 21.36]
        decList = ["+24:18:00.00",  24.3,  "+24:18:00.00",  -28.25, -15.32]

        from astrocalc.coords import coordinates_to_array
        ra, dec = coordinates_to_array(
            log=log,
            ra=raList,
            dec=decList
        )

        print ra, dec

        from astrocalc.coords import coordinates_to_array
        ra, dec = coordinates_to_array(
            log=log,
            ra="13:20:00.00",
            dec="+24:18:00.00"
        )

        print ra, dec

    def test_coordinates_to_array_function_exception(self):

        from astrocalc.coords import coordinates_to_array
        try:
            this = coordinates_to_array(
                log=log,
                settings=settings,
                fakeKey="break the code"
            )
            this.get()
            assert False
        except Exception, e:
            assert True
            print str(e)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
