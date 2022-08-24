# Copyright 2022 Amethyst Reese
# Licensed under the MIT license
# flake8: noqa

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .app import app

# from .mc import mc, mcdict, Cacheable
from . import encoder
from .routing import context, api, get, post
from .template import template
