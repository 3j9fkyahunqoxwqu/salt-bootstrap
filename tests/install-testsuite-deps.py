#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    install-testsuite-deps.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Install the required dependencies to properly run the test-suite.

    :codeauthor: :email:`Pedro Algarvio (pedro@algarvio.me)`
    :copyright: © 2013 by the SaltStack Team, see AUTHORS for more details.
    :license: Apache 2.0, see LICENSE for more details.
'''

import sys
import subprocess
from bootstrap import GRAINS

COMMANDS = []
if GRAINS['os'] == 'SmartOS':
    COMMANDS.extend([
        'pkgin up',
        'pkgin -y in scmgit-base py27-pip',
        'pip install unittest2'
    ])
elif GRAINS['os'] == 'openSUSE':
    COMMANDS.extend([
        'zypper --non-interactive addrepo --refresh http://download.opensuse.org/repositories'
        '/devel:/languages:/python/{0}/devel:languages:python.repo'.format(
            GRAINS['osrelease']
        ),
        'zypper --gpg-auto-import-keys --non-interactive refresh',
        'zypper --non-interactive install --auto-agree-with-licenses git python-pip',
        'pip install unittest2'
    ])
else:
    print(
        'Failed gather the proper commands to allow the tests suite to be '
        'executed in this system.\nSystem Grains:\n{0}'.format(
            GRAINS
        )
    )
    sys.exit(1)


for command in COMMANDS:
    print 'Executing {0!r}'.format(command)
    process = subprocess.Popen(command, shell=True)
    process.communicate()

print('\nDONE\n')
exit(0)
