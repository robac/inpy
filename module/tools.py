import constants

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

def process_action(event_action):
    elements = str.split(event_action, ":")
    print len(elements)
    #return events, action