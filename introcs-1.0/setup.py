#-----------------------------------------------------------------------
# setup.py
# Install script for the "Introduction to Programming in Python"
# code library.
# Author: Bob Dondero
#-----------------------------------------------------------------------

from distutils.core import setup
from setuptools.command.install import install
from os import chmod

class MyInstall(install):
    def run(self):
        # Perform a normal install.
        install.run(self)
        # Change permissions of the installed .py and .pyc files.
        for fileName in self.get_outputs():
            if fileName.endswith(('.py', '.pyc')):
                chmod(fileName, 420)  # 420 decimal = 644 octal

setup(
    name='introcs',
    author='Robert Sedgewick, Kevin Wayne, Robert Dondero',
    author_email='[rs,wayne,rdondero]@cs.princeton.edu',
    description=\
        'Code library for the book Intro. to Programming in Python',
    version='1.0',
    py_modules=['color', 'instream', 'outstream', 'picture', 
        'stdarray', 'stdaudio', 'stddraw', 'stdio', 'stdrandom', 
        'stdstats'],
    cmdclass={'install': MyInstall}
)

