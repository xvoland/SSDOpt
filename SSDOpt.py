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

print "\x1b[1;32m"
print "********************************************************************"
print "* SSD OPTIMIZATION v0.1 Installer for Mac OS X                     *"
print "* I'd be glad to see most of you at our page http://www.dotoca.net *"
print "********************************************************************"
print "\x1b[0m"


def request_yesno(question, default='yes'):
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

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return default
        elif choice in valid.keys():
            return valid[choice]
        else:
            sys.stdout.write('Please respond: "yes/no" or y/n.\n')


def request_input(question, range, default=-1):
    """
    Input request value to the user from range
    with default value if it's set

    return: integer value from range
    """
    if default < 0:
        # if not set value by default
        default = range[0]

    # expect proper input
    while True:
        try:
            enter = raw_input(question + ' : %s' % default + chr(8) * len(str(default)))
            if not enter:
                enter = default
            else:
                enter = int(enter)

            # entered value in range
            if enter in range:
                return enter
            else:
                sys.stdout.write('\x1b[1;31m' + 'Error: value must be from %s till %s\x1b[0m\n' % (range[0], range[-1]))

        except ValueError:
            print('\x1b[1;31m' + 'Error: value must be integer! Please enter correct value' + '\x1b[0m')


def run():
    PATH_TO_SCRIPT = '/Library/StartupItems/RamFS/'
    SCRIPT_NAME = 'RamFS'

    # check if running on Mac
    mac = (platform.system() == 'Darwin')
    
    # get current username
    currentUser = commands.getoutput('whoami')

    if os.path.exists(PATH_TO_SCRIPT + SCRIPT_NAME):
        print('\x1b[1;31m' + 'It appears that the SSDOpt or RamFS has already installed. Please, remove and try again.' + '\x1b[0m')

    # check if sudo, getuid doesn't return 0 if sudoing
    if os.getuid() != 0:
        print('\x1b[1;31m' + 'Please, re-start with ROOT privileges, i.e. "sudo python ./install.py"' + '\x1b[0m')
        exit()


if __name__ == '__main__':
    # a = request_input('Please enter size of virtual drive', (4, 50))
    # print a
    run()
