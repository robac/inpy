import yaml

def read_config_file(file):
    with open(file, 'r') as stream:
        try:
            config = yaml.load(stream)
            status = "OK"
        except yaml.YAMLError as exc:
            config = {}
            status = exc.message
    return status, config

def check_config(config):
    return "OK"

def process_config_file(file):
    config, status = read_config_file(file)
    if not status == "OK":
        return status, config
    valid = check_config(config)
    if not valid == "OK":
        status = valid
    return status, config

