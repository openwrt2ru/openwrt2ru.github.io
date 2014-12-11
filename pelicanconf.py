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

# Social widget
#SOCIAL = (('OpenWRT', 'http://openwrt.org/'),)

MENUITEMS = (('Блог', '/category/blog.html'),
             ('Руководства', '/category/tutorials.html'),
             ('Термины', '/category/glossary.html'),
             ('FAQ', '/category/faq.html'),
             ('О проекте', '/category/about.html'),)

PLUGINS = [
	'pelican_vimeo',
]

DEFAULT_PAGINATION = 10
USE_FOLDER_AS_CATEGORY = True

DISPLAY_PAGES_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
