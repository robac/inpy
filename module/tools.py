import constants

def event_mask_from_text(text, separator = constants.CONF_EVENT_SEPARATOR):
    values = str.split(text, separator)
    values = [ x.strip() for x in values]


    #for v in values:
     #   if

    return values