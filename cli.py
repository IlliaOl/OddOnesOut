import argparse
import checker

# TODO add documentation
# TODO check arguments
my_parser = argparse.ArgumentParser(prog='checker',
                                    description='moves files with specific extension to a specific folder')
my_parser.add_argument('-c', action='store', type=str, nargs=3)

args = my_parser.parse_args()


checker.move_files(*args.c)
