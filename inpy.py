import sys

import defaults
from module import arguments
from module import configuration
from module import logger
from module import constants


ARGUMENTS = {}
CONFIG = {}

def process_arguments():
    global ARGUMENTS
    ARGUMENTS = arguments.read_arguments(sys.argv[1:], defaults.DEFAULT_ARGUMENTS)

def process_config_file():
    global CONFIG
    status, CONFIG = configuration.process_config_file(ARGUMENTS[constants.CONFIG_FILE_ARGUMENT])
    return status

def watch():
    for key in CONFIG[constants.WATCH_SECTION]:
        print(key)

def main():
    """
    process_arguments()

    status = process_config_file()
    print status
    if not status == "OK":
        print (status)
        sys.exit(3)
    print CONFIG
    watch()
    """
    logger.init_syslogger(constants.LOG_DEBUG)
    logger.init_filelogger('/tmp/inpy.log', constants.LOG_DEBUG)
    logger.log(constants.LOG_CRITICAL, "hello inpy", constants.LOGTO_FILELOG | constants.LOGTO_SYSLOG)

if __name__ == "__main__":
    main()


