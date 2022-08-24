# Copyright 2022 Amethyst Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from functools import wraps
import re

from flask import make_response, render_template, request
from jinja2.utils import Markup

from . import app, encoder
from .routing import fullpath, _titles

whitespace_regex = re.compile(r'\s*(</?[^>]+>)\s*')


def template(template, status=200, minify=False):
    """Use the given template for the page, using the returned dictionary for
    template values."""
    def decorator(f):
        template_name = fullpath(template, base='')

        @wraps(f)
        def decorated_function(*args, **kwargs):
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx

            update_template_parameters(ctx)
            output = render_template(template_name, **ctx)

            if minify:
                output = whitespace_regex.sub(r'\1', output)

            return make_response(output, status)
        return decorated_function
    return decorator


def update_template_parameters(params):
    """Modify the given dictionary of template parameters with default
    values."""
    for key in ('GA_ACCOUNT', 'SITE_DOMAIN', 'SITE_PROTOCOL', 'SITE_ROOT'):
        if key in app.config:
            params[key] = app.config[key]

    if 'title' not in params and request.path in _titles:
        params['title'] = _titles[request.path]


@app.template_filter()
def time(t=None, f='%Y-%m-%d %I:%M %p'):
    """Format a timestamp to year, month, day, hour, and minutes."""
    import time
    if t is None:
        t = time.time()
    s = time.strftime(f, time.gmtime(t))
    return s


@app.template_filter()
def date(t=None, f='%Y-%m-%d'):
    """Format a timestamp to year, month, and day."""
    return time(t, f)


@app.template_filter()
def count(o):
    """Output the length of the given iterable object."""
    return len(o)


@app.template_filter()
def json(o):
    """Dump an object to json."""
    return Markup(encoder.dumps(o))


@app.template_filter()
def url(u):
    """Convert a service-absolute path to a site-absolute path."""
    return fullpath(u)
