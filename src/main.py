import opencolumbus.argutil as argutil
import opencolumbus.parcels as parcels
import os, sys

# TODO TESTME
def ensure_dir_exists(loc):
  if os.path.isdir(loc):
    return True
  elif os.path.exists(loc):
    raise Exception('Error: data directory already exists as a file!')
  else:
    os.mkdir(loc)
    return True

# TODO TESTME
def run_module(module_name, args):
  '''Invokes the selected module.'''
  if module_name == 'parcels':
    parcels.run(args)
  else:
    raise Exception('Unknown module %s' % module_name)

# TODO TESTME
def main(argv):
  parser = argutil.mk_parser()
  args = parser.parse_args(argv)

  ensure_dir_exists(args.data_dir)

  for module in args.modules:
    run_module(module, args)

if __name__ == '__main__':
  main(sys.argv[1:])

