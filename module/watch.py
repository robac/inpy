import constants
import inotify.adapters
import logger
import os

watches = []


def add_watches(adapter, watch_config):
    for watch_key in watch_config.keys():
        watch_item = watch_config[watch_key]
        if watch_item[constants.CONF_ITEM_RECURSIVE]:
            add_recursive_watch(adapter, watch_item[constants.CONF_ITEM_DIRECTORY])
        else:
            add_watch(adapter, watch_item[constants.CONF_ITEM_DIRECTORY])


def add_watch(adapter, path):
    adapter.add_watch(path)
    watches.append(path)
    logger.log(constants.LOG_INFO, "added watch " + path)

def add_recursive_watch(adapter, path):
    q = [path]
    while q:
        current_path = q[0]
        del q[0]

        add_watch(adapter, current_path)

        for filename in os.listdir(current_path):
            entry_filepath = os.path.join(current_path, filename)
            if os.path.isdir(entry_filepath) is False:
                continue

            q.append(entry_filepath)


def remove_watches(adapter):
    for path in watches:
        adapter.remove_watch(constants.CONF_ITEM_DIRECTORY)
        logger.log(constants.LOG_INFO, "removed watch " + path)


def watch(watch_config):
    adapter = inotify.adapters.Inotify()
    add_watches(adapter, watch_config)

    try:
        for event in adapter.event_gen():
            if event is not None:
                (header, type_names, watch_path, filename) = event
                logger.log(constants.LOG_INFO, watch_path+filename)
    finally:
        remove_watches(adapter)



