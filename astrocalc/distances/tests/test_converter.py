from __future__ import print_function
from builtins import str
import os
import unittest
import shutil
import unittest
import yaml
from astrocalc.utKit import utKit
from fundamentals import tools
from os.path import expanduser
home = expanduser("~")

packageDirectory = utKit("").get_project_root()
settingsFile = packageDirectory + "/test_settings.yaml"
su = tools(
    arguments={"settingsFile": settingsFile},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName=None,
    defaultSettingsFile=False
)
arguments, settings, log, dbConn = su.setup()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

try:
    shutil.rmtree(pathToOutputDir)
except:
    pass
# COPY INPUT TO OUTPUT DIR
shutil.copytree(pathToInputDir, pathToOutputDir)

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)


class test_converter(unittest.TestCase):

    def test_converter_function01(self):

        from astrocalc.distances import converter
        c = converter(log=log)

        dists = c.redshift_to_distance(
            z=0.108,
            WM=0.3,
            WV=0.7,
            H0=70.0
        )

        print(dists)

    def test_converter_function02(self):

        from astrocalc.distances import converter
        c = converter(log=log)

        dists = c.distance_to_redshift(
            mpc=500
        )

        print(dists)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
