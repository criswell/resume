#!/usr/bin/env python

import sys, datetime, os, subprocess
try:
    from jinja2 import Template
    from jinja2 import FileSystemLoader
    from jinja2.environment import Environment
except ImportError:
    print("Uh-oh! Looks like you don't have jinja2 installed!")
    print("Go to http://jinja.pocoo.org/ and install it please!")
    sys.exit(1)

hg_id = 'Unknown'
hg_branch = 'Unknown'
hg_update = 'Unknown'

def usage():
    print("jinga_build.py file.html repo_directory <templateDirectories>")
    print("\nBuilds a file specified by 'file.html', dumping to STDOUT the resulting HTML.\n")
    print("<templateDirectories> is one or more directories for templates to be housed,")
    print("separated by commas.\n")
    print("'repo_directory' is the path to the hg repo containing the resume builder.")

def runcmd(cmd):
    return subprocess.check_output(cmd.split(' '))

if len(sys.argv) < 2 or len(sys.argv) > 4:
    usage()
    sys.exit()

filename = sys.argv[1]
templateFile = open(filename, 'r')
rawTemplate = templateFile.readlines()
templateFile.close()

#hg_branch = runcmd('git symbolic-ref HEAD 2>/dev/null')

#if hgapi:
#    repo = hgapi.Repo(sys.argv[2])
#    hg_id = repo.hg_id()
#    hg_branch = repo.hg_branch()
#    hg_update = repo.revision(hg_id)

strTemplate = "".join(rawTemplate)

env = Environment()
if len(sys.argv) == 4:
    p = sys.argv[3].split(',')
    env.loader = FileSystemLoader(p)
else:
    env.loader = FileSystemLoader(".")

builder = {
            'date' : '%s' % datetime.datetime.now(),
#            'id' : hg_id,
#            'branch' : hg_branch,
#            'updated' : hg_update.date
        }

template = env.from_string(strTemplate)
rendered = template.render(builder=builder)

print(rendered)

