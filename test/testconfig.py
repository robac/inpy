from module import arguments
import inotify.constants

EVENT_LOOKUP = {}

def test(text):
    EVENT_LOOKUP = dict((k, v) for v, k in inotify.constants.MASK_LOOKUP.iteritems())
    print(EVENT_LOOKUP)