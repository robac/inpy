import logging
import logging.handlers




my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')
handler = logging.handlers.RotatingFileHandler('/var/log/inpy.log')

my_logger.addHandler(handler)



def log():
    print "test"
    my_logger.critical('this is critical')