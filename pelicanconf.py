#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'openwrt2ru Team'
SITENAME = u'OpenWRT to Russian'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

THEME = 'themes/gum'

DEFAULT_LANG = u'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('OpenWRT', 'http://openwrt.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

MENUITEMS = (('О проекте', '/about.html'),
             ('Загрузки', '/downloads.html'),
             ('Документация', '/documentation.html'),
             )

PLUGINS = [
	'pelican_vimeo',
]

DEFAULT_PAGINATION = 10
USE_FOLDER_AS_CATEGORY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
