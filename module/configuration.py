import yaml
import constants

def read_config_file(file):
    with open(file, 'r') as stream:
        try:
            config = yaml.load(stream)
            status = "OK"
        except yaml.YAMLError as exc:
            config = {}
            status = exc.message
    return status, config

def transform_watch_section(config):
    new_watch = {}
    print (config[constants.CONF_SEC_WATCH][0].keys()[0])
    for watch_item in config[constants.CONF_SEC_WATCH]:
        key = watch_item.keys()[0]
        new_watch[key] = watch_item[key]
    config[constants.CONF_SEC_WATCH] = new_watch


def check_config(config):
    return "OK"

def process_config_file(file):
    status, config = read_config_file(file)
    if not status == "OK":
        return status, config
    transform_watch_section(config)

    valid = check_config(config)
    if not valid == "OK":
        status = valid
    return status, config

