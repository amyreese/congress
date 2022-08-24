# Copyright 2022 Amethyst Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json

from queue import LifoQueue
from os import path

from future.moves.urllib.parse import urlparse
from past.builtins import basestring

from core import app
from .trigger import Trigger


class Congress(object):
    _instance = None

    def __init__(self):
        self.load_triggers()

    def search(self, query):
        '''Given a search query, return a valid URL with the search result.'''

        match, trigger = self.match_query(query)

        if not match:
            match = self.fallback.pattern.match(query)
            return self.fallback.render(query, match)

        result = trigger.render(query, match)
        parts = urlparse(result)

        if parts.scheme and parts.netloc:
            return result

        # allow triggers to chain from other triggers
        return self.search(result)

    def match_query(self, query):
        '''Given a search query, return a tuple containing a regex match and
        trigger object that matches the given query.  If no match can be found,
        return a tuple of (None, None).'''

        sink = LifoQueue()

        while not self.triggers.empty():
            trigger = self.triggers.get()
            match = trigger.pattern.match(query)

            if match:
                break

            else:
                sink.put(trigger)
                trigger = None

        while not sink.empty():
            self.triggers.put(sink.get())

        if trigger:
            self.triggers.put(trigger)
            return (match, trigger)

        return (None, None)

    def load_triggers(self):
        '''Read from all the trigger definition files listed in config value
        TRIGGER_PATHS, and add them all to a LIFO queue.'''

        self.fallback = Trigger(url=app.config['DEFAULT_SEARCH'], pattern='')
        self.triggers = LifoQueue()
        count = 0

        for filepath in app.config['TRIGGER_PATHS']:
            if not path.isfile(filepath):
                app.logger.warning('trigger path %s not found', filepath)
                continue

            with open(filepath) as f:
                triggers = json.loads(f.read())

            if not isinstance(triggers, dict):
                app.logger.warning('trigger path %s has invalid structure',
                                   filepath)
                continue

            for pattern, value in triggers.items():
                if isinstance(value, basestring):
                    trigger = Trigger(url=value, pattern=pattern)

                elif isinstance(value, dict):
                    trigger = Trigger(data=value, pattern=pattern)

                else:
                    # don't know what to do with anything else atm
                    continue

                self.triggers.put(trigger)
                count += 1

        app.logger.info('loaded %d triggers', count)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = Congress()

        return cls._instance
