# Copyright 2015 John Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json


class Encoder(json.JSONEncoder):
    def default(self, o):
        try:
            return o._encode()
        except:
            return str(o)


def dump(obj, pretty=True):
    indent = None
    if pretty:
        indent = 4

    return json.dumps(obj, cls=Encoder, indent=indent)
dumps = dump


def load(s):
    return json.loads(s)


def idify(name):
    """Create an ID string from a name by replacing periods and spaces with
    underscores."""
    return name.replace(' ', '_').replace('.', '_').lower()
