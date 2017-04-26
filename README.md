# inpy

config file:
    * YAML
    * two main sections: general (general settings, log file etc.), watch (list of directories to watch)

general (keys):
    * log-file: string; log file location
    * syslog: boolean;

watch (list):
    * name of item
    * keys:
            * directory: string; directory to watch
            * recursive: boolean; is watcher recursive?
            * event: inotify events to bind
            * action: string; action to run
