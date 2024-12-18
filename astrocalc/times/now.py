#!/usr/local/bin/python
# encoding: utf-8
"""
*Report current time in various formats*

Author
: David Young
"""
from __future__ import division
from past.utils import old_div
from builtins import object
import sys
import os
import math
import time
os.environ['TERM'] = 'vt100'


class now(object):
    """
    *Report the current time into various formats*

    **Key Arguments**

    - ``log`` -- logger
    - ``settings`` -- the settings dictionary

    """
    # Initialisation

    def __init__(
            self,
            log,
            settings=False,

    ):
        self.log = log
        log.debug("instansiating a new 'now' object")
        self.settings = settings
        # xt-self-arg-tmpx

        # Initial Actions

        return None

    def get_mjd(self):
        """
        *Get the current time as an MJD*

        **Return**

        - ``mjd`` -- the current MJD as a float


        **Usage**


        .. todo::

            - add clutil
            - remove `getCurrentMJD` from all other code

        ```python
        from astrocalc.times import now
        mjd = now(
            log=log
        ).get_mjd()
        ```
        """
        self.log.debug('starting the ``get_mjd`` method')

        jd = old_div(time.time(), 86400.0) + 2440587.5
        mjd = jd - 2400000.5

        self.log.debug('completed the ``get_mjd`` method')
        return mjd

    # xt-class-method
