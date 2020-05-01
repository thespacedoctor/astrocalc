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

# SETUP PATHS TO COMMON DIRECTORIES FOR TEST DATA
pathToInputDir = moduleDirectory + "/input/"
pathToOutputDir = moduleDirectory + "/output/"

try:
    shutil.rmtree(pathToOutputDir)
except:
    pass
# COPY INPUT TO OUTPUT DIR
shutil.copytree(pathToInputDir, pathToOutputDir)

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)


class test_coordinates_to_array(unittest.TestCase):

    def test_coordinates_to_array(self):

        raList = ["13:20:00.00", 200.0, "13:20:00.00", 175.23, 21.36]
        decList = ["+24:18:00.00",  24.3,  "+24:18:00.00",  -28.25, -15.32]

        from astrocalc.coords import coordinates_to_array
        ra, dec = coordinates_to_array(
            log=log,
            ra=raList,
            dec=decList
        )

        print(ra, dec)

        from astrocalc.coords import coordinates_to_array
        ra, dec = coordinates_to_array(
            log=log,
            ra="13:20:00.00",
            dec="+24:18:00.00"
        )

        print(ra, dec)

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
        except Exception as e:
            assert True
            print(str(e))

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
