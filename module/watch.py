import constants
import inotify.adapters
import logger

def set_watch(watch_config):
    adapter = inotify.adapters.Inotify()
    adapter.add_watch(b'/tmp')
    try:
        for event in adapter.event_gen():
            if event is not None:
                (header, type_names, watch_path, filename) = event
                logger.log(constants.LOG_INFO, watch_path+filename)
    finally:
        adapter.remove_watch(b'/tmp')

    #for i in watch_config.keys():


