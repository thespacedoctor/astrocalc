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


class test_separations(unittest.TestCase):

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
        print(calculator.get())

        calculator = separations(
            log=log,
            ra1=2.3342343,
            dec1=89.23244233,
            ra2=45.343545345,
            dec2=87.3435435
        )
        print(calculator.get())

        calculator = separations(
            log=log,
            ra1=352.5342343,
            dec1=89.23,
            ra2="23:32:34.642",
            dec2="89:12:34.9334"
        )
        print(calculator.get())

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
