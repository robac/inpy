import constants
import pyinotify

def set_watch(watch_config):
    for i in watch_config.keys():
        print(i)
        print(watch_config[i])
