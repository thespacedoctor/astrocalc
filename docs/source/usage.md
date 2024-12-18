

```bash
    
    Documentation for astrocalc can be found here: http://astrocalc.readthedocs.org
    
    Usage:
        astrocalc [-c] coordflip <ra> <dec>
        astrocalc sep <ra1> <dec1> <ra2> <dec2>
        astrocalc timeflip <datetime>
        astrocalc trans <ra> <dec> <north> <east>
        astrocalc now mjd
        astrocalc dist <distVal> (z|mpc) [--hc=<hVal> --wm=<OmegaMatter> --wv=<OmegaVacuum>]
    
    Commands:
        coordflip             flip coordinates between decimal degrees and sexegesimal and vice-versa
        sep                   calculate the separation between two locations in the sky.
        timeflip              flip time between UT and MJD.
        trans                 translate a location across the sky (north and east in arcsec)
        now                   report current time in various formats
        dist                  convert distance between mpc to z
    
    Variables:
        ra, ra1, ra2          right-ascension in deciaml degrees or sexegesimal format
        dec, dec1, dec2       declination in deciaml degrees or sexegesimal format
        datetime              modified julian date (mjd) or universal time (UT). UT can be formated 20150415113334.343 or "20150415 11:33:34.343" (spaces require quotes)
        north, east           vector components in arcsec
        distVal               a distance value in Mpc (-mpc) or redshift (-z)
        hVal                  hubble constant value. Default=70 km/s/Mpc
        OmegaMatter           Omega Matter. Default=0.3
        OmegaVacuum           Omega Vacuum. Default=0.7
    
    Options:
        -v, --version                           show version
        -h, --help                              show this help message
        -m, --mpc                               distance in mpc
        -z, --redshift                          redshift distance
        -c, --cartesian                         convert to cartesian coordinates
        -s, --settings <pathToSettingsFile>     the settings file
    

```
