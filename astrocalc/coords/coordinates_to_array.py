#!/usr/local/bin/python
# encoding: utf-8
"""
*Convert single values of RA, DEC or list of RA and DEC to numpy arrays*

Author
: David Young
"""
from astrocalc.coords import unit_conversion
import sys
import os
os.environ['TERM'] = 'vt100'


def coordinates_to_array(
        log,
        ra,
        dec):
    """*Convert a single value RA, DEC or list of RA and DEC to numpy arrays*

    **Key Arguments**

    - ``ra`` -- list, numpy array or single ra value
    - ``dec`` --list, numpy array or single dec value
    - ``log`` -- logger


    **Return**

    - ``raArray`` -- input RAs as a numpy array of decimal degree values
    - ``decArray`` -- input DECs as a numpy array of decimal degree values


    **Usage**

    .. todo::

        add usage info
        create a sublime snippet for usage

    ```python
    ra, dec = coordinates_to_array(
        log=log,
        ra=ra,
        dec=dec
    )
    ```

    """
    log.debug('starting the ``coordinates_to_array`` function')

    import numpy as np

    if isinstance(ra, np.ndarray) and isinstance(dec, np.ndarray):
        return ra, dec

    # ASTROCALC UNIT CONVERTER OBJECT
    converter = unit_conversion(
        log=log
    )
    # CONVERT RA AND DEC TO NUMPY ARRAYS
    if isinstance(ra, float):
        pass
    elif isinstance(ra, ("".__class__, u"".__class__)):
        try:
            ra = float(ra)
        except:
            ra = converter.ra_sexegesimal_to_decimal(ra=ra)
    elif isinstance(ra, list):
        try:
            ra = np.array(ra).astype(np.float)
        except:
            raList = []
            raList[:] = [converter.ra_sexegesimal_to_decimal(ra=r) for r in ra]
            ra = raList

    if isinstance(dec, float):
        pass
    elif isinstance(dec, ("".__class__, u"".__class__)):
        try:
            dec = float(dec)
        except:
            dec = converter.dec_sexegesimal_to_decimal(dec=dec)
    elif isinstance(dec, list):
        try:
            dec = np.array(dec).astype(np.float)
        except:
            decList = []
            decList[:] = [
                converter.dec_sexegesimal_to_decimal(dec=d) for d in dec]
            dec = decList

    raArray = np.array(ra, dtype='f8', ndmin=1, copy=True)
    decArray = np.array(dec, dtype='f8', ndmin=1, copy=True)

    log.debug('completed the ``coordinates_to_array`` function')
    return raArray, decArray
