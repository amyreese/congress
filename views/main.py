# Copyright 2014 John Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import abort
from jinja2.filters import do_capitalize

from core import app, context, get, template

@get('/', 'Index')
@template('index.html')
def index():
    return {}

