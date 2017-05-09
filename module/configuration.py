import yaml
import constants
import exception
import tools
from pprint import  pprint

def read_config_file(file):
    with open(file, 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as exc:
            config = {}
            """
            raise exception.ConfigurationError(
                constants.ERROR_LOADING_YAML_FILE_MSG.format(exc.context_mark.name),
                constants.ERROR_LOADING_YAML_FILE_DET.format(
                    exc.problem,
                    exc.context_mark.line,
                    exc.context_mark.column
            ))
            """
            raise exception.ConfigurationError("error loading configuration file", "")
    return config

def transform_action_section(watch_item):
    new_action = {}
    for action_item in watch_item[constants.CONF_SEC_ACTION]:
        key = action_item.keys()[0]
        new_action[tools.event_mask_from_text(key)] = action_item[key]
    return new_action


def transform_watch_section(config):
    new_watch = {}
    print config
    for watch_item in config[constants.CONF_SEC_WATCH]:
        key = watch_item.keys()[0]
        new_watch[key] = watch_item[key]
        new_watch[key][constants.CONF_SEC_ACTION] = transform_action_section(new_watch[key])
    config[constants.CONF_SEC_WATCH] = new_watch


def process_action(event_action):
    elements = str.split(event_action, ":")
    print len(elements)



def check_config(config):
    return True

def process_config_file(file):
    config = read_config_file(file)

    transform_watch_section(config)

    valid = check_config(config)
    if not valid:
        raise exception.ConfigurationError("Not valis")
    return config

