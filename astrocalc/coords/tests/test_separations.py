import os
import nose
import shutil
import yaml
from astrocalc.coords import separations
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


class test_separations():

    def test_separations_function(self):
        # xt-kwarg_key_and_value

        from astrocalc.coords import separations
        calculator = separations(
            log=log,
            ra1="23:32:23.2324",
            dec1="-13:32:45.43553",
            ra2="23:32:34.642",
            dec2="-12:12:34.9334",
        )
        print calculator.get()

        from astrocalc.coords import separations
        calculator = separations(
            log=log,
            ra1=2.3342343,
            dec1=89.23244233,
            ra2=45.343545345,
            dec2=87.3435435
        )
        print calculator.get()

        from astrocalc.coords import separations
        calculator = separations(
            log=log,
            ra1=352.5342343,
            dec1=89.23,
            ra2="23:32:34.642",
            dec2="89:12:34.9334"
        )
        print calculator.get()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
