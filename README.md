astrocalc
=========

*An astronomer's calculator used to perform common calculations,
conversions and measurements.*.

Usage
=====

    astrocalc coordflip <ra> <dec>
    astrocalc sep <ra1> <dec1> <ra2> <dec2>

    coordflip             flip coordinates between decimal degrees and sexegesimal and vice-versa
    sep                   calculate the separation between two locations in the sky.
    -h, --help            show this help message

Documentation
=============

Documentation for astrocalc is hosted by [Read the
Docs](http://astrocalc.readthedocs.org/en/stable/) (last [stable
version](http://astrocalc.readthedocs.org/en/stable/) and [latest
version](http://astrocalc.readthedocs.org/en/latest/)).

Installation
============

The easiest way to install astrocalc us to use `pip`:

    pip install astrocalc

Or you can clone the [github
repo](https://github.com/thespacedoctor/astrocalc) and install from a
local version of the code:

    git clone git@github.com:thespacedoctor/astrocalc.git
    cd astrocalc
    python setup.py install

To upgrade to the latest version of astrocalc use the command:

    pip install astrocalc --upgrade

Development
-----------

If you want to tinker with the code, then install in development mode.
This means you can modify the code from your cloned repo:

    git clone git@github.com:thespacedoctor/astrocalc.git
    cd astrocalc
    python setup.py develop

[Pull requests](https://github.com/thespacedoctor/astrocalc/pulls) are
welcomed!

Issues
------

Please report any issues
[here](https://github.com/thespacedoctor/astrocalc/issues).

License
=======

Copyright (c) 2016 David Young

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
