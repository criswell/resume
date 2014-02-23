
What is it?
===========

Sam's resume repo, really....

Basically, I *hate* writing my resume. I hate maintaining it; I hate all the
BS self-aggrandizing you have to do when writing it; I hate *everything* you
have to do when working on one.

Additionally, I *hate* the tools a lot of people wind up using to create them.
I hate word processors; I hate non-standard formats that can only be read on
specific platforms; I hate having to write documents in GUIs.

To solve these problems, I wrote my resume in valid HTML5 (meaning any browser
that does its job can render it) and I wrote it in a way that makes updating
it easier for me.

Basically, I scripted my resume :-P

How do I build it?
==================

My resume builder utilizes makefiles, a Python script, and some libraries. If
you wish you build it, you need a Python interpretor (2.5+ I'd guess), a
working makefile interpreter (GNU make is lovely), and the following Python
modules:

* [Jinja2](http://jinja.pocoo.org/)
* [hgapi](http://pypi.python.org/pypi/hgapi/)

I'd suggest setting up a virtualenv environment with these, but do whatever
you want.

Once this is done, you can build and test the resume with:

    $ make clean ; make test

This will build the resume, place it in output/, and report whether the
document is valid HTML5 or not.

You can also do rudimentary spell checking using:

    $ make spell

Note that this requires [links](http://links.twibright.com/) and [GNU
Aspell](http://aspell.net/) to work.

What does the end result look like?
===================================

My latest resume builds can be found here:

* [criswell.bitbucket.org](http://criswell.bitbucket.org/)

What is "experimental"?
=======================

Inside the repo is an "experimental" directory. This is where I place anything
I'm toying with that might be remotely related to the resume.

Copyright
=========

Unless otherwise specified, everything in here is available under the license
stipulated by COPYING, which is the CC0 1.0 Universal license. Basically, it
places everything in as close to the public domain as I can do so with a
license.

