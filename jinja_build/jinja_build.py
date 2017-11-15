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

#hg_id = 'Unknown'
git_branch = 'Unknown'
git_update = 'Unknown'

def usage():
    print("jinga_build.py file.html repo_directory <templateDirectories>")
    print("\nBuilds a file specified by 'file.html', dumping to STDOUT the resulting HTML.\n")
    print("<templateDirectories> is one or more directories for templates to be housed,")
    print("separated by commas.\n")
    print("'repo_directory' is the path to the hg repo containing the resume builder.")

def runcmd(cmd):
    return subprocess.check_output(cmd.split(' '))

def get_current_branch():
    current_branch = None
    try:
        current_branch = runcmd('git symbolic-ref -q --short HEAD')
        current_branch = current_branch.strip()
    except subprocess.CalledProcessError:
        current_branch = None

    if isinstance(current_branch, bytes):
        current_branch = current_branch.decode('utf-8')
    return current_branch

def get_latest_update():
    update_date = None
    try:
        o = runcmd('git cat-file commit HEAD')
        if isinstance(o, bytes):
            o = o.decode('utf-8')
        lines = o.split('\n')
        for i in lines:
            if i.startswith('author '):
                l = i.split(' ')[-2]
                update_date = datetime.datetime.fromtimestamp(
                        int(l)).strftime('%Y-%m-%d %H:%M:%S')
                break
    except subprocess.CalledProcessError:
        update_date = None

    return update_date

def get_rev_id():
    revid = None
    try:
        revid = runcmd('git rev-parse HEAD')
        revid = revid.strip()
    except subprocess.CalledProcessError:
        revid = None

    if isinstance(revid, bytes):
        revid = revid.decode('utf-8')
    return revid

if len(sys.argv) < 2 or len(sys.argv) > 4:
    usage()
    sys.exit()

filename = sys.argv[1]
templateFile = open(filename, 'r')
rawTemplate = templateFile.readlines()
templateFile.close()

commit_id = get_rev_id()
git_branch = get_current_branch()
git_update = get_latest_update()

strTemplate = "".join(rawTemplate)

env = Environment()
if len(sys.argv) == 4:
    p = sys.argv[3].split(',')
    env.loader = FileSystemLoader(p)
else:
    env.loader = FileSystemLoader(".")

builder = {
            'date' : '%s' % datetime.datetime.now(),
            'id' : commit_id,
            'branch' : git_branch,
            'updated' : git_update
        }

template = env.from_string(strTemplate)
rendered = template.render(builder=builder)

print(rendered)

