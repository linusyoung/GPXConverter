#setup.py
from distutils.core import setup
setup(
  name = 'gpxconverter',
  packages = ['gpxconverter'], # this must be the same as the name above
  version = '0.1',
  description = 'gpx to csv converter',
  author = 'Linus Yang',
  author_email = 'linusyoungrice@gmail.com',
  url = 'https://github.com/linusyoung/GPXConverter', # use the URL to the github repo
  download_url = 'https://github.com/linusyoung/GPXConverter/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['gpx', 'converter', 'csv'], # arbitrary keywords
  classifiers = [],
)