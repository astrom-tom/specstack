from setuptools import setup
import catmatch.__main__ as cats


__version__ = '19.4.0'
__place__ = 'ESO, Santiago'
__credits__ = "Romain Thomas"
__license__ = "GNU GPL v3"
__maintainer__ = "Romain Thomas"
__email__ = "the.spartan.proj@gmail.com"
__status__ = "released"
__website__ = "https://astrom-tom.github.io/dfitspy/build/html/index.html"


setup(
   name = 'specstack',
   version = __version__,
   author = __credits__,
   packages = ['specstack'],
   entry_points = {'gui_scripts': ['specstack = specstack.__main__:main',],},
   description = 'A simple catalog matching script',
   python_requires = '>=3.6',
   install_requires = [
       "numpy >= 1.16",
       "catscii>= 1.1",
   ],
   include_package_data=True,
)
