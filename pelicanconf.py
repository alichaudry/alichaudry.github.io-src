#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ali Chaudry'
SITENAME = "Ali's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Mulberry', 'https://getmulberry.com'),
         ('Columbia', 'https://columbia.edu'),
         ('UAlbany', 'https://albany.edu'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://linkedin.com/in/alihchaudry/'),
          ('Twitter', 'https://twitter.com/manjanjatx'),
          ('StackOverflow', 'https://stackoverflow.com/users/5076471/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# added by ali
TYPOGRIFY = True
THEME = '../pelican-themes/elegant'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['tipue_search']

DIRECT_TEMPLATES = ['search', 'tags', '404', 'index', 'categories', 'archives']

TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
SEARCH_URL = "search"
LANDING_PAGE_TITLE = 'I am me.'
SITE_LICENSE = """Content licensed under <a rel="license nofollow noopener noreferrer"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Attribution 4.0 International License</a>."""
USE_SHORTCUT_ICONS = True
STATIC_PATHS = ['theme/images', 'images']
