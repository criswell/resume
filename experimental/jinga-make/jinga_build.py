#!/usr/bin/env python

import sys
from jinja2 import Template

def usage():
    print "jinga_build.py file.html"
    print "\nBuilds a file specified by 'file.html', dumping to STDOUT the resulting HTML."

if len(sys.argv) != 1:
    usage()
    sys.exit()

filename = sys.argv[0]
templateFile = open(filename, 'r')
rawTemplate = templateFile.readlines()
templateFile.close()

template = Template(rawTemplate)
template.render()

