#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Setting OS X to store temporary files and files that are not important
for the system in RAM rather than on disk.

Based on the idea by:
    - Ricardo Gameiro <http://blogs.nullvision.com/?p=357>
    - Daniel Jenkins <http://blogs.nullvision.com/?p=357#comment-1140>

*** ATTENTION !!! ***
I DON'T TAKE ANY RESPONSIBILITY FOR THE CONSEQUENCES OF SCRIPT.
HOPE YOU ENJOY USING THIS SCRIPT

Good luck,
    Vitalii Tereshchuk / [xVoLAnD]
"""

import os
import sys
import platform
import commands

os.system('clear')

print '********************************************************************'
print '* SSD OPTIMIZATION v0.1 Installer for Mac OS X                     *'
print '* I\'d be glad to see most of you at our page http://www.dotoca.net *'
print '********************************************************************'

# check if running on Mac
mac = (platform.system() == 'Darwin')

# check if root, getuid doesn't return 0 if sudoing
currentUser = commands.getoutput('whoami')
if currentUser != 'root':
    print 'Please, re-start with ROOT privileges, i.e. "sudo python ./install.py"\n'
    sys.exit()


def yes_no(question, default='yes'):
    """
    Question to the user: (yes/no) or (y/n) not case sensitive

    return: yes|no
    """
    valid = {'yes': 'yes',
               'y': 'yes',
              'no': 'no',
               'n': 'no'
    }

    if default == None:
        prompt = ' [y/n] '
    elif default == 'yes':
        prompt = ' [Y/n] '
    elif default == 'no':
        prompt = ' [y/N] '
    else:
        raise ValueError('Invalid default answer: "%s"' % default)

    while 1:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return default
        elif choice in valid.keys():
            return valid[choice]
        else:
            sys.stdout.write('Please respond: "yes/no" or y/n.\n')

