import argparse

# TODO TESTME
def mk_parser():
  parser = argparse.ArgumentParser('Retrieve and process public data from Columbus, OH')

  parser.add_argument('--modules', dest='modules', nargs='+', help='Which modules to run. Choices: parcels')
  parser.add_argument('--data-dir', required=False, default='./data', help='Location of the data output directory')

  return parser

