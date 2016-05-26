Usage
======

.. code-block:: bash 
   
    astrocalc coordflip <ra> <dec>
    astrocalc sep <ra1> <dec1> <ra2> <dec2>
    astrocalc timeflip <datetime>
    astrocalc trans <ra> <dec> <north> <east>

    coordflip             flip coordinates between decimal degrees and sexegesimal and vice-versa
    sep                   calculate the separation between two locations in the sky.
    timeflip              flip time between UT and MJD. <datetime> within in MJD or UT
    trans                 translate a location across the sky (north and east in arcsec)
    -h, --help            show this help message
    