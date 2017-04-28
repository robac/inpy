"""
DEFAULT_ARGUMENTS = {
   'config-file' : 
	{
		'value' : '/etc/inpy/config.yml',
		'description' : 'path to config file',
		'has-argument' : True
	},
   'log-file' : 
	{
		'value' : '/var/log/inpy.log',
		'description' : 'path to log file',
		'has-argument' : False
	}
}
"""
from module import constants

DEFAULT_ARGUMENTS = {
   constants.ARGUMENT_CONFIG_FILE:
	{
		constants.ARGUMENT_VALUE 		: '/etc/inpy/config.yml',
		constants.ARGUMENT_DESCRIPTION 	: 'path to config file',
		constants.ARGUMENT_HAS_ARGUMENT : True
	},
   constants.ARGUMENT_LOG_FILE:
	{
		constants.ARGUMENT_VALUE       	: '/var/log/inpy.log',
		constants.ARGUMENT_DESCRIPTION 	: 'path to log file',
		constants.ARGUMENT_HAS_ARGUMENT : False
	}
}

