import inotify.constants

EVENT_LOOKUP  = dict((k, v) for v, k in inotify.constants.MASK_LOOKUP.iteritems())

ACTION_REGEXP = '^\s*({0})(\s*,\s*({0}))*\s*:.*$'

ARGUMENT_CONFIG_FILE    = 'config-file'
ARGUMENT_LOG_FILE       = 'log-file'
ARGUMENT_HAS_ARGUMENT   = 'has-argument'
ARGUMENT_VALUE          = 'value'
ARGUMENT_DESCRIPTION    = 'description'

#configuration file
#section names
CONF_SEC_WATCH          = 'watch'
CONF_SEC_GENERAL        = 'general'
CONF_SEC_WATCH          = 'action'

#item names
CONF_ITEM_DIRECTORY     = 'directory'
CONF_ITEM_RECURSIVE     = 'recursive'

#event separator in action section
CONF_EVENT_SEPARATOR    = ','

LOG_CRITICAL = 50
LOG_ERROR = 40
LOG_WARNING = 30
LOG_INFO = 20
LOG_DEBUG = 10
LOG_NOTSET = 0

LOGTO_SYSLOG = 1
LOGTO_FILELOG = 2

ERROR_LOADING_YAML_FILE_MSG = 'Error loading YAML file {}.'
ERROR_LOADING_YAML_FILE_DET = 'Reason: {}. Line: {}. Column: {}'
