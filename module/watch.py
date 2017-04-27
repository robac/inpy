import constants
import inotify.adapters
import logger

watches = []

def add_watch(adapter, path):
    adapter.add_watch(path)
    watches.append(path)
    logger.log(constants.LOG_INFO, "added watch " + path)

def remove_watches(adapter):
    for path in watches:
        adapter.remove_watch(constants.CONF_ITEM_DIRECTORY)
        logger.log(constants.LOG_INFO, "removed watch " + path)


def watch(watch_config):
    adapter = inotify.adapters.Inotify()
    for watch_key in watch_config.keys():
        watch_item = watch_config[watch_key]
        add_watch(adapter, watch_item[constants.CONF_ITEM_DIRECTORY])

    try:
        for event in adapter.event_gen():
            if event is not None:
                (header, type_names, watch_path, filename) = event
                logger.log(constants.LOG_INFO, watch_path+filename)
    finally:
        for watch_key in watch_config.keys():
            watch_item = watch_config[watch_key]
            remove_watches(adapter)

    #for i in watch_config.keys():


