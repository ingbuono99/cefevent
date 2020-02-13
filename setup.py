import os
from distutils.core import setup

long_description = 'ArcSight Common Event Format library'
if os.path.exists('README.md'):
    long_description = open('README.md', 'r').read()


setup(
  name = 'cefevent',
  packages = ['cefevent'],
  version = '0.5',
  description = 'ArcSight Common Event Format library',
  long_description = long_description,
  author = 'Kamus Hadenes',
  author_email = 'kamushadenes@hyadesinc.com',
  url = 'https://github.com/kamushadenes/cefevent',
  download_url = 'https://github.com/kamushadenes/cefevent/tarball/0.5',
  keywords = ['logging', 'cef', 'arcsight', 'event', 'security'],
)
