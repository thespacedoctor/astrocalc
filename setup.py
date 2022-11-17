from setuptools import setup, find_packages
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))
exec(open(moduleDirectory + "/astrocalc/__version__.py").read())


def readme():
    with open(moduleDirectory + '/README.md') as f:
        return f.read()


install_requires = [
    'pyyaml',
    'numpy',
    'fundamentals'

]

# READ THE DOCS SERVERS
exists = os.path.exists("/home/docs/")
if exists:
    c_exclude_list = ['healpy', 'astropy',
                      'numpy', 'sherlock', 'wcsaxes', 'HMpTy', 'ligo-gracedb']
    for e in c_exclude_list:
        try:
            install_requires.remove(e)
        except:
            pass

setup(name="astrocalc",
      version=__version__,
      description="perform common astronomy-related calculations, conversions and measurements within python scripts or from the command-line",
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
          'Topic :: Utilities',
      ],
      keywords=['astronomy, calculate, convert'],
      url='https://github.com/thespacedoctor/astrocalc',
      download_url='https://github.com/thespacedoctor/astrocalc/archive/v%(__version__)s.zip' % locals(
      ),
      author='David Young',
      author_email='davidrobertyoung@gmail.com',
      license='MIT',
      packages=find_packages(exclude=["*tests*"]),
      include_package_data=True,
      install_requires=install_requires,
      test_suite='nose2.collector.collector',
      tests_require=['nose2', 'cov-core'],
      entry_points={
          'console_scripts': ['astrocalc=astrocalc.cl_utils:main'],
      },
      zip_safe=False)
