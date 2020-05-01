from __future__ import print_function
from builtins import str
import os
import unittest
import shutil
import unittest
import yaml
from fundamentals import tools
from astrocalc.utKit import utKit
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

class test_translate(unittest.TestCase):

    def test_translate_function01(self):

        from astrocalc.coords import translate
        ra, dec = translate(
            log=log,
            settings=settings,
            ra="14:45:32.3432",
            dec="-45:34:23.3434",
            northArcsec=45,
            eastArcsec=68
        ).get()

        print(ra, dec)

    def test_translate_function02(self):

        from astrocalc.coords import translate
        ra, dec = translate(
            log=log,
            settings=settings,
            ra="14.546",
            dec="-45.34232334",
            northArcsec=4560,
            eastArcsec=-5678
        ).get()

        print(ra, dec)

    def test_translate_ra_gt_360(self):

        from astrocalc.coords import translate
        ra, dec = translate(
            log=log,
            settings=settings,
            ra="14.546438",
            dec="-45.34232",
            northArcsec=4560,
            eastArcsec=+967800
        ).get()

        print(ra, dec)

    def test_translate_ra_lt_360(self):

        from astrocalc.coords import translate
        ra, dec = translate(
            log=log,
            settings=settings,
            ra="14.546438",
            dec="-45.34232334",
            northArcsec=4560,
            eastArcsec=-967800
        ).get()

        print(ra, dec)

    def test_translate_dec_lt_m90(self):

        from astrocalc.coords import translate
        ra, dec = translate(
            log=log,
            settings=settings,
            ra="14.546438",
            dec="-85.34",
            northArcsec=-43560,
            eastArcsec=-967800
        ).get()

        print(ra, dec)

    def test_translate_dec_gt_90(self):

        from astrocalc.coords import translate
        ra, dec = translate(
            log=log,
            settings=settings,
            ra="14.546438",
            dec="85.34232334",
            northArcsec=45600,
            eastArcsec=-967800
        ).get()

        print(ra, dec)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
