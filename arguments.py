import getopt
import sys
import pprint


def print_usage(values):
    print("Usage:") 
    print("\t--help\t\t\tprint usage message")
    for key, value in values.iteritems():
	print("\t--"+key+"\t\t"+value['description'])

def compose_options(values):
    options = []
    for key, value in values.iteritems():
        option = key
        if value['argument']:
	   option = option + "="
        options.append(option)	
    options.append('help')
    return options

def compose_default_arguments(values):
    arguments = {}
    for key, value in values.iteritems():
        arguments[key] = value['value'] 
    return arguments

def read_arguments(arguments, default_values):
    options = compose_options(default_values)
    def_arguments = compose_default_arguments(default_values)
    try:
        opts, args = getopt.getopt(arguments, "", options)
    except getopt.GetoptError as err:
        print(err)
        print_usage(default_values)
        sys.exit(2)
    for o, a in opts:
        if o == "--help":
            print_usage(default_values)
	    sys.exit()
        elif o[2:] in def_arguments:
            def_arguments[o[2:]] = a
        else:
            assert False, "unhandled option"
    return def_arguments

    
