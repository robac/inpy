import sys

import defaults
from module import arguments
from module import configuration
from module import logger
from module import constants
from module import watch
import inotify.adapters
import inotify.constants
from test import testconfig
from module import tools
from module import exception


ARGUMENTS = {}
CONFIG = {}

def process_arguments():
    global ARGUMENTS
    ARGUMENTS = arguments.read_arguments(sys.argv[1:], defaults.DEFAULT_ARGUMENTS)

def process_config_file():
    global CONFIG
    CONFIG = configuration.process_config_file(ARGUMENTS[constants.ARGUMENT_CONFIG_FILE])

def main():
    logger.init_syslogger(constants.LOG_INFO)
    logger.log(constants.LOG_INFO, "start inpy")

    try:
        process_arguments()
        process_config_file()
        print CONFIG
    except exception.ConfigurationError as exc:
        print exc.message
        print exc.detail
        sys.exit(3)



    #watch.watch(CONFIG[constants.CONF_SEC_WATCH])

    logger.log(constants.LOG_INFO, "close inpy")


if __name__ == "__main__":
    main()


