import logging
import logging.handlers
import constants

syslogger = None;
logger = None;


def init_syslogger(loglevel):
    global syslogger
    syslogger = logging.getLogger('inpy_syslogger')
    syslogger.setLevel(loglevel)
    handler = logging.handlers.SysLogHandler(address = '/dev/log')
    syslogger.addHandler(handler)

def init_filelogger(file, loglevel):
    global logger
    logger = logging.getLogger('inpy_filelogger')
    logger.setLevel(loglevel)
    handler = logging.handlers.RotatingFileHandler(file)
    logger.addHandler(handler)

def log(level, message, where=None):
    if where is None:
        where = constants.LOGTO_SYSLOG
    if where & constants.LOGTO_SYSLOG:
        syslogger.log(level, message)
    if where & constants.LOGTO_FILELOG:
        logger.log(level, message)