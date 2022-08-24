# Copyright 2022 Amethyst Reese
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from congress import Congress
from core import get, template
from flask import redirect


@get('/', 'Search')
@template('/index.html')
def query(q=''):
    if q:
        url = Congress.instance().search(q)
        return redirect(url)

    else:
        return {}


@get('/s', 'Search')
@template('/search.html')
def search(q=''):
    url = Congress.instance().search(q)

    return {'url': url}


@get('/opensearch.xml', 'Congress')
@template('/opensearch.xml')
def opensearch():
    return {}
