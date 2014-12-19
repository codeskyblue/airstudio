# coding: utf-8
#

from setuptools import setup, find_packages
import airstudio

long_description = ''
try:
    with open('README.md') as f:
        long_description = f.read()
except:
    pass

setup(
      name='airstudio',
      version=airstudio.__version__,
      description='web ide for air test utils',
      long_description=long_description,

      author='codeskyblue',
      author_email='codeskyblue@gmail.com',

      packages = find_packages(),
      include_package_data=True,
      package_data={},
      install_requires=[
          'click >= 3.3',
          'humanize >= 0.5',
          'requests >= 2.4.3', 
          'Flask >= 0.10.1',
          'aircv >= 1.01',
          ],
      entry_points='''
      [console_scripts]
      air.studio = airstudio:main
      ''')
