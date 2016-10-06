from setuptools import setup, find_packages
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))
exec(open(moduleDirectory + "/astrocalc/__version__.py").read())


def readme():
    with open(moduleDirectory + '/README.rst') as f:
        return f.read()


setup(name="astrocalc",
      version=__version__,
      description="An astronomer's calculator used to perform common calculations, conversions and measurements.",
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
      ],
      keywords=['tools', 'astronomy'],
      url='https://github.com/thespacedoctor/astrocalc',
      download_url='https://github.com/thespacedoctor/astrocalc/archive/v%(__version__)s.zip' % locals(
      ),
      author='David Young',
      author_email='davidrobertyoung@gmail.com',
      license='MIT',
      packages=find_packages(),
      package_data={'astrocalc': [
          'resources/*/*', 'resources/*.*']},
      include_package_data=True,
      install_requires=[
          'pyyaml',
          'fundamentals',
          'numpy'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['astrocalc=astrocalc.cl_utils:main'],
      },
      zip_safe=False)
