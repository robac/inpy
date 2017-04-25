# inpy

config file:
    * YAML
    * two main sections: general (general settings, log file etc.), watch (list of directories to watch)

general (keys):
    * log-file: log file location

watch (list):
    * name of item
    * keys:
            * directory: directory to watch
            * recursive: is watcher recursive?
            * event: inotify events to bind
            * action:
