import sys

import defaults
from module import arguments
from module import configuration
from module import logger
from module import constants
from module import watch
import inotify.adapters
from test import testconfig
from module import tools


ARGUMENTS = {}
CONFIG = {}

def process_arguments():
    global ARGUMENTS
    ARGUMENTS = arguments.read_arguments(sys.argv[1:], defaults.DEFAULT_ARGUMENTS)

def process_config_file():
    global CONFIG
    status, CONFIG = configuration.process_config_file(ARGUMENTS[constants.ARGUMENT_CONFIG_FILE])
    return status

def main():
    print tools.event_mask_from_text('IN_CREATE, IN_ISDIR      ')
    sys.exit()


    logger.init_syslogger(constants.LOG_INFO)
    logger.log(constants.LOG_INFO, "start inpy")

    process_arguments()
    status = process_config_file()
    print status
    if not status == "OK":
        print (status)
        sys.exit(3)
    watch.watch(CONFIG[constants.CONF_SEC_WATCH])

    logger.log(constants.LOG_INFO, "close inpy")


if __name__ == "__main__":
    main()


