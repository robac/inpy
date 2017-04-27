import constants
import inotify.adapters
import inotify.constants
import logger
import os

watches = {}
kill_now = False

def add_watches(adapter, watch_config):
    for watch_key in watch_config.keys():
        watch_item = watch_config[watch_key]
        if watch_item[constants.CONF_ITEM_RECURSIVE]:
            add_recursive_watch(adapter, watch_item[constants.CONF_ITEM_DIRECTORY])
        else:
            add_watch(adapter, watch_item[constants.CONF_ITEM_DIRECTORY])
    print(watches)


def add_watch(adapter, path, recursive=False):
    adapter.add_watch(path, inotify.constants.IN_CREATE | inotify.constants.IN_ISDIR)
    watches[path] = {
            'recursive': recursive
        }
    logger.log(constants.LOG_INFO, "added watch " + path)


def add_recursive_watch(adapter, path):
    q = [path]
    while q:
        current_path = q[0]
        del q[0]

        add_watch(adapter, current_path, True)

        for filename in os.listdir(current_path):
            entry_filepath = os.path.join(current_path, filename)
            if os.path.isdir(entry_filepath) is False:
                continue
            q.append(entry_filepath)


def remove_watches(adapter):
    print("watche remove")
    for entry in watches:
        path = entry['path']
        adapter.remove_watch(path)
        logger.log(constants.LOG_INFO, "removed watch " + path)


def watch_loop(adapter):
    try:
        for event in adapter.event_gen():
            if event is not None:
                (header, type_names, watch_path, filename) = event
                if (header.mask & (inotify.constants.IN_ISDIR | inotify.constants.IN_CREATE)) > 0:
                    if watches[watch_path]['recursive']:
                        add_watch(adapter, os.path.join(watch_path, filename), True)

    finally:
        None



def watch(watch_config):
    adapter = inotify.adapters.Inotify()
    add_watches(adapter, watch_config)

    print(watches)

    try:
        watch_loop(adapter)
    finally:
        logger.log(constants.LOG_CRITICAL, "END END END")
        remove_watches(adapter)



