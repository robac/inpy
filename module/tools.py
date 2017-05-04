import constants
import re

def event_mask_from_text(text, separator = constants.CONF_EVENT_SEPARATOR):
    values = str.split(text, separator)
    values = [ v.strip() for v in values]

    mask = 0
    for v in values:
        if v in constants.EVENT_LOOKUP:
            mask = mask | constants.EVENT_LOOKUP[v]
        else:
            raise Exception("Chyba")

    return mask


def get_all_events_regexp():
    start = True
    for k in constants.EVENT_LOOKUP:
        if start:
            start = False
            res = k
        else:
            res += '|'+k
    return res


def validate_action(text):
    pattern = constants.ACTION_REGEXP.format(get_all_events_regexp())
    print pattern
    match = re.search(pattern, text)
    if match is None:
        return False
    else:
        return True


def process_action(event_action):
    elements = str.split(event_action, ":")
    print len(elements)
    #return events, action

