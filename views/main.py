# Copyright 2015 John Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from core import get, template


@get('/', 'Index')
@template('index.html')
def index():
    return {}
