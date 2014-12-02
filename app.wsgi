# Copyright 2014 John Reese
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
import views

if __name__ == '__main__':
    if sys.flags.interactive:
        print("debug shell")

        print(">>> from core import app")

    else:
        app.run()
