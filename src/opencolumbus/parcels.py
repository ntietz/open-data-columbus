import urllib

import shutil
import urllib2
from contextlib import closing

LATEST_SHAPEFILES_URL = 'ftp://apps.franklincountyauditor.com/GIS_Shapefiles/2016/09/20160926_parcel.zip'
LATEST_CSV_URL = 'ftp://apps.franklincountyauditor.com/Parcel_CSV/2016/10/parcel.csv'

# TODO TESTME
def run(args):
  '''Retrieves and processes all the data that Columbus releases about parsels.'''
  get_from_ftp(LATEST_CSV_URL, '%s/%s' % (args.data_dir, 'parcel.csv'))
  get_from_ftp(LATEST_SHAPEFILES_URL, '%s/%s' % (args.data_dir, 'parcel_shapefiles.zip'))

def get_from_ftp(ftp_path, out_path):
  print 'Downloading %s, saving to %s...' % (ftp_path, out_path)
  with closing(urllib2.urlopen(ftp_path)) as ftp_file:
    with open(out_path, 'wb') as out_file:
      shutil.copyfileobj(ftp_file, out_file)
  print 'Download complete!'

