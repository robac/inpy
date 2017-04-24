import sys

import defaults
from lib import test, arguments, configuration

ARGUMENTS = {}
CONFIG = {}

def process_arguments():
    global ARGUMENTS
    ARGUMENTS = arguments.read_arguments(sys.argv[1:], defaults.DEFAULT_ARGUMENTS)

def process_config_file():
    status, CONFIG = configuration.process_config_file(ARGUMENTS['config-file'])
    return status

def main():
    test.test()
    sys.exit()
    process_arguments()
    status = process_config_file()
    print status
    if not status == "OK":
        print (status)
        sys.exit(3)
    print CONFIG

if __name__ == "__main__":
    main()


