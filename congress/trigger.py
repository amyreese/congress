# Copyright 2015 John Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re

from ent import Ent


class Trigger(Ent):

    def __init__(self, pattern='_', url='', **kwargs):
        pattern = re.compile(pattern, re.IGNORECASE)
        super(Trigger, self).__init__(pattern=pattern, url=url, **kwargs)

    def render(self, query, match):
        positional = match.groups()
        named = match.groupdict()
        params = query[match.end():].strip()

        return self.url.format(
            *positional, query=query, params=params, **named,
        )
