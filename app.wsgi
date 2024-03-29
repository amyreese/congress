# Copyright 2022 Amethyst Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from os import path
import sys

cwd = path.abspath(path.dirname(__file__))
sys.path.insert(0, cwd)

os.environ['APP_PATH'] = cwd

from core import app
from core import app as application
import views

if __name__ == '__main__':
    interactive = sys.flags.interactive
    try:
        __IPYTHON__
        interactive = True
    except NameError:
        pass

    if interactive:
        print("\ncongress debug shell")
        print(">>> from core import app")

        from congress import Congress
        print(">>> from congress import Congress")

    if '--no-run' in sys.argv:
        pass

    else:
        print('running')
        app.run()
