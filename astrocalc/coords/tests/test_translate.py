import os
import nose
import shutil
import yaml
from astrocalc.coords import translate
from astrocalc.utKit import utKit

from fundamentals import tools

su = tools(
    arguments={"settingsFile": None},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName="astrocalc.coords"
)
arguments, settings, log, dbConn = su.setup()

# load settings
stream = file(
    "/Users/Dave/.config/astrocalc.coords/astrocalc.coords.yaml", 'r')
settings = yaml.load(stream)
stream.close()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()


class test_translate():

    def test_translate_function01(self):

        ra, dec = translate(
            log=log,
            settings=settings,
            ra="14:45:32.3432",
            dec="-45:34:23.3434",
            northArcsec=45,
            eastArcsec=68
        ).get()

        print ra, dec

    def test_translate_function02(self):

        ra, dec = translate(
            log=log,
            settings=settings,
            ra="14.546",
            dec="-45.34232334",
            northArcsec=4560,
            eastArcsec=-5678
        ).get()

        print ra, dec

    def test_translate_ra_gt_360(self):
        ra, dec = translate(
            log=log,
            settings=settings,
            ra="14.546438",
            dec="-45.34232",
            northArcsec=4560,
            eastArcsec=+967800
        ).get()

        print ra, dec

    def test_translate_ra_lt_360(self):
        ra, dec = translate(
            log=log,
            settings=settings,
            ra="14.546438",
            dec="-45.34232334",
            northArcsec=4560,
            eastArcsec=-967800
        ).get()

        print ra, dec

    def test_translate_dec_lt_m90(self):
        ra, dec = translate(
            log=log,
            settings=settings,
            ra="14.546438",
            dec="-85.34",
            northArcsec=-43560,
            eastArcsec=-967800
        ).get()

        print ra, dec

    def test_translate_dec_gt_90(self):
        ra, dec = translate(
            log=log,
            settings=settings,
            ra="14.546438",
            dec="85.34232334",
            northArcsec=45600,
            eastArcsec=-967800
        ).get()

        print ra, dec

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
