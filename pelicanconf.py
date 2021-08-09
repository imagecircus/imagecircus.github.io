#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ian Dow-Wright'
SITENAME = 'idw.xyz'
# Theme Settings
THEME = 'themes/idwxyz'
SITEDESCRIPTION = 'desc'
FAVICON = 'pelly.png'
LOGO = 'pelly.png'
FIRST_NAME = 'Ian'
STATIC_PATHS=['img']
DISPLAY_CATEGORIES_ON_MENU = False

SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

PLUGIN = 'neighbors'

MARKDOWN = {

    "extension_configs": {

        'markdown.extensions.meta': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        "mdx_video": {},
    },
    "output_format": "html5",
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True