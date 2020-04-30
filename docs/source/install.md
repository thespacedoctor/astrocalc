# Installation

The easiest way to install astrocalc is to use `pip` (here we show the install inside of a conda environment):

``` bash
conda create -n astrocalc python=3.7 pip
conda activate astrocalc
pip install astrocalc
```

Or you can clone the [github repo](https://github.com/thespacedoctor/astrocalc) and install from a local version of the code:

``` bash
git clone git@github.com:thespacedoctor/astrocalc.git
cd astrocalc
python setup.py install
```

To upgrade to the latest version of astrocalc use the command:

``` bash
pip install astrocalc --upgrade
```

To check installation was successful run `astrocalc -v`. This should return the version number of the install.

## Development

If you want to tinker with the code, then install in development mode. This means you can modify the code from your cloned repo:

``` bash
git clone git@github.com:thespacedoctor/astrocalc.git
cd astrocalc
python setup.py develop
```

[Pull requests](https://github.com/thespacedoctor/astrocalc/pulls) are welcomed! 

<!-- ### Sublime Snippets

If you use [Sublime Text](https://www.sublimetext.com/) as your code editor, and you're planning to develop your own python code with soxspipe, you might find [my Sublime Snippets](https://github.com/thespacedoctor/astrocalc-Sublime-Snippets) useful. -->


