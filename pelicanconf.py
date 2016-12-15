#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Cl\xe9ment Albert'
SITETITLE = u'Cl\xe9ment Albert'
SITESUBTITLE = u'Doctorant en Mathématiques Appliquées'
SITENAME = u'Cl\xe9ment Albert'
SITEURL = ''

SITELOGO = SITEURL + '/files/20160421_095137.jpg'

PATH = 'content'
STATIC_PATHS = ['files']

THEME = 'themes/Flex'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-cite']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PAGES_SORT_ATTRIBUTE='order'
