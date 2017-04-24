import getopt
import sys
import pprint
import arguments
import defaults
import configuration

ARGUMENTS = {}
CONFIG = {}

def process_arguments():
    global ARGUMENTS
    ARGUMENTS = arguments.read_arguments(sys.argv[1:], defaults.DEFAULT_ARGUMENTS)

def process_config_file():
    status, config = configuration.process_config_file(ARGUMENTS['config-file'])
    print status

def main():
    process_arguments()
    process_config_file()
    print ARGUMENTS

if __name__ == "__main__":
    main()


