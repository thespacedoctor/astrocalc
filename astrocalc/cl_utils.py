#!/usr/local/bin/python
# encoding: utf-8
"""
Documentation for astrocalc can be found here: http://astrocalc.readthedocs.org/en/stable

Usage:
    astrocalc [-c] coordflip <ra> <dec>
    astrocalc sep <ra1> <dec1> <ra2> <dec2>
    astrocalc timeflip <datetime>
    astrocalc trans <ra> <dec> <north> <east>
    astrocalc now mjd
    astrocalc dist (-z | -m) <distVal> [--hc=hVal --wm=OmegaMatter --wv=OmegaVacuum]


    COMMANDS:
    ========
        coordflip             flip coordinates between decimal degrees and sexegesimal and vice-versa
        sep                   calculate the separation between two locations in the sky.
        timeflip              flip time between UT and MJD.
        trans                 translate a location across the sky (north and east in arcsec)
        now                   report current time in various formats
        dist                  convert distance between mpc to z

    VARIABLES:
    ==========
        ra, ra1, ra2          right-ascension in deciaml degrees or sexegesimal format
        dec, dec1, dec2       declination in deciaml degrees or sexegesimal format
        datetime              modified julian date (mjd) or universal time (UT). UT can be formated 20150415113334.343 or "20150415 11:33:34.343" (spaces require quotes)
        north, east           vector components in arcsec
        distVal               a distance value in Mpc (-mpc) or redshift (-z)
        hVal                  hubble constant value. Default=70 km/s/Mpc
        OmegaMatter           Omega Matter. Default=0.3
        OmegaVacuum           Omega Vacuum. Default=0.7

    -h, --help            show this help message
    -m, --mpc             distance in mpc
    -z, --redshift        redshift distance
    -c, --cartesian       convert to cartesian coordinates

"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
import readline
import glob
import pickle
from docopt import docopt
from fundamentals import tools, times
from astrocalc.coords import unit_conversion
# from ..__init__ import *


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]


def main(arguments=None):
    """
    *The main function used when ``cl_utils.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    from astrocalc.coords import unit_conversion
    # setup the command-line util settings
    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="CRITICAL",
        options_first=True,
        projectName="astrocalc"
    )
    arguments, settings, log, dbConn = su.setup()

    # tab completion for raw_input
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(tab_complete)

    # unpack remaining cl arguments using `exec` to setup the variable names
    # automatically
    for arg, val in arguments.iteritems():
        if arg[0] == "-":
            varname = arg.replace("-", "") + "Flag"
        else:
            varname = arg.replace("<", "").replace(">", "")
        if isinstance(val, str) or isinstance(val, unicode):
            exec(varname + " = '%s'" % (val,))
        else:
            exec(varname + " = %s" % (val,))
        if arg == "--dbConn":
            dbConn = val
        log.debug('%s = %s' % (varname, val,))

    ## START LOGGING ##
    startTime = times.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE cl_utils.py AT %s' %
        (startTime,))

    # set options interactively if user requests
    if "interactiveFlag" in locals() and interactiveFlag:

        # load previous settings
        moduleDirectory = os.path.dirname(__file__) + "/resources"
        pathToPickleFile = "%(moduleDirectory)s/previousSettings.p" % locals()
        try:
            with open(pathToPickleFile):
                pass
            previousSettingsExist = True
        except:
            previousSettingsExist = False
        previousSettings = {}
        if previousSettingsExist:
            previousSettings = pickle.load(open(pathToPickleFile, "rb"))

        # x-raw-input
        # x-boolean-raw-input
        # x-raw-input-with-default-value-from-previous-settings

        # save the most recently used requests
        pickleMeObjects = []
        pickleMe = {}
        theseLocals = locals()
        for k in pickleMeObjects:
            pickleMe[k] = theseLocals[k]
        pickle.dump(pickleMe, open(pathToPickleFile, "wb"))

    # CALL FUNCTIONS/OBJECTS
    if coordflip:

        if cartesianFlag:
            converter = unit_conversion(
                log=log
            )
            x, y, z = converter.ra_dec_to_cartesian(
                ra="23 45 21.23232",
                dec="+01:58:5.45341"
            )
            print x, y, z
            return

        try:
            ra = float(ra)
            dec = float(dec)
            degree = True
        except Exception, e:
            degree = False

        if degree is True:
            converter = unit_conversion(
                log=log
            )
            try:
                ra = converter.ra_decimal_to_sexegesimal(
                    ra=ra,
                    delimiter=":"
                )
                dec = converter.dec_decimal_to_sexegesimal(
                    dec=dec,
                    delimiter=":"
                )
            except Exception, e:
                print e
                sys.exit(0)

            print ra, dec
        else:
            converter = unit_conversion(
                log=log
            )
            try:
                ra = converter.ra_sexegesimal_to_decimal(
                    ra=ra
                )
                dec = converter.dec_sexegesimal_to_decimal(
                    dec=dec
                )
            except Exception, e:
                print e
                sys.exit(0)
            print ra, dec

    if sep:
        from astrocalc.coords import separations
        calculator = separations(
            log=log,
            ra1=ra1,
            dec1=dec1,
            ra2=ra2,
            dec2=dec2,
        )
        angularSeparation, north, east = calculator.get()
        print """%(angularSeparation)s arcsec (%(north)s N, %(east)s E)""" % locals()

    if timeflip:
        try:
            inputMjd = float(datetime)
            if datetime[0] not in ["0", "1", "2"]:
                inputMjd = True
            else:
                inputMjd = False
        except:
            inputMjd = False
        from astrocalc.times import conversions
        converter = conversions(
            log=log
        )

        if inputMjd == False:
            try:
                mjd = converter.ut_datetime_to_mjd(utDatetime=datetime)
                print mjd
            except Exception, e:
                print e
        else:
            try:
                utDate = converter.mjd_to_ut_datetime(mjd=datetime)
                print utDate
            except Exception, e:
                print e

    if trans:
        # TRANSLATE COORDINATES ACROSS SKY
        from astrocalc.coords import translate
        newRa, newDec = translate(
            log=log,
            ra=ra,
            dec=dec,
            northArcsec=float(north),
            eastArcsec=float(east)
        ).get()
        from astrocalc.coords import unit_conversion
        converter = unit_conversion(
            log=log
        )
        ra = converter.ra_decimal_to_sexegesimal(
            ra=newRa,
            delimiter=":"
        )
        dec = converter.dec_decimal_to_sexegesimal(
            dec=newDec,
            delimiter=":"
        )

        print "%(newRa)s, %(newDec)s (%(ra)s, %(dec)s)" % locals()

    if now:
        from astrocalc.times import now
        mjd = now(
            log=log
        ).get_mjd()
        print mjd

    if dist and redshiftFlag:
        from astrocalc.distances import converter
        c = converter(log=log)
        if not hcFlag:
            hcFlag = 70.
        if not wmFlag:
            wmFlag = 0.3
        if not wvFlag:
            wvFlag = 0.7
        dists = c.redshift_to_distance(
            z=float(distVal),
            WM=float(wmFlag),
            WV=float(wvFlag),
            H0=float(hcFlag)
        )
        print "Distance Modulus: " + str(dists["dmod"]) + " mag"
        print "Luminousity Distance: " + str(dists["dl_mpc"]) + " Mpc"
        print "Angular Size Scale: " + str(dists["da_scale"]) + " kpc/arcsec"
        print "Angular Size Distance: " + str(dists["da_mpc"]) + " Mpc"
        print "Comoving Radial Distance: " + str(dists["dcmr_mpc"]) + " Mpc"

    if dist and mpcFlag:
        from astrocalc.distances import converter
        c = converter(log=log)
        z = c.distance_to_redshift(
            mpc=float(distVal)
        )
        print "z = %(z)s" % locals()

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE cl_utils.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return


if __name__ == '__main__':
    main()
