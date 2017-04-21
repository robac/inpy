import getopt
import sys
import pprint
import arguments
import defaults

ARGUMENTS = {}


def main():
    ARGUMENTS = arguments.read_arguments(sys.argv[1:], defaults.DEFAULT_ARGUMENTS)

if __name__ == "__main__":
    main()
