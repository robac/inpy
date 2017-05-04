import inotify.constants

EVENT_LOOKUP  = dict((k, v) for v, k in inotify.constants.MASK_LOOKUP.iteritems())

ACTION_REGEXP = r"^\s*((IN_CREATE|IN_NECO|IN_MASTO)\s*,\s*)*(IN_CREATE|IN_NECO|IN_MASTO):.*$"

ARGUMENT_CONFIG_FILE    = 'config-file'
ARGUMENT_LOG_FILE       = 'log-file'
ARGUMENT_HAS_ARGUMENT   = 'has-argument'
ARGUMENT_VALUE          = 'value'
ARGUMENT_DESCRIPTION    = 'description'

CONF_SEC_WATCH          = 'watch'
CONF_SEC_GENERAL        = 'general'
CONF_ITEM_DIRECTORY     = 'directory'
CONF_ITEM_RECURSIVE     = 'recursive'
CONF_EVENT_SEPARATOR    = ','

LOG_CRITICAL = 50
LOG_ERROR = 40
LOG_WARNING = 30
LOG_INFO = 20
LOG_DEBUG = 10
LOG_NOTSET = 0

LOGTO_SYSLOG = 1
LOGTO_FILELOG = 2

ERROR_LOADING_YAML_FILE = 'Error loading YAML file %s'