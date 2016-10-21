import os
import nose
import shutil
import yaml
from astrocalc.distances import converter
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


class test_converter():

    def test_converter_function01(self):

        from astrocalc.distances import converter
        c = converter(log=log)

        dists = c.redshift_to_distance(
            z=0.108,
            WM=0.3,
            WV=0.7,
            H0=70.0
        )

        print dists

    def test_converter_function02(self):

        from astrocalc.distances import converter
        c = converter(log=log)

        dists = c.distance_to_redshift(
            mpc=500
        )

        print dists

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
