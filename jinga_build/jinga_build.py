#!/usr/bin/env python

import sys
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

def usage():
    print "jinga_build.py file.html <templateDirectories>"
    print "\nBuilds a file specified by 'file.html', dumping to STDOUT the resulting HTML."
    print "<templateDirectories> is one or more directories for templates to be housed,"
    print "separated by commas."

if len(sys.argv) < 2 or len(sys.argv) > 3:
    usage()
    sys.exit()

filename = sys.argv[1]
templateFile = open(filename, 'r')
rawTemplate = templateFile.readlines()
templateFile.close()

strTemplate = "".join(rawTemplate)
#print strTemplate

env = Environment()
if len(sys.argv) == 3:
    p = sys.argv[2].split(',')
    env.loader = FileSystemLoader(p)
else:
    env.loader = FileSystemLoader(".")

template = env.from_string(strTemplate)
rendered = template.render()

print rendered

