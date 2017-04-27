import sys

import defaults
from module import arguments
from module import configuration
from module import logger
from module import constants
from module import watch
import inotify.adapters


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
    logger.init_syslogger(constants.LOG_INFO)
    logger.log(constants.LOG_INFO, "start inpy")

    process_arguments()
    status = process_config_file()
    print status
    if not status == "OK":
        print (status)
        sys.exit(3)
    watch.set_watch(CONFIG[constants.CONF_SEC_WATCH])

    logger.log(constants.LOG_INFO, "close inpy")


if __name__ == "__main__":
    main()


