#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'lizherui'
SITENAME = u"lizherui's blog"
SITEURL = 'http://lizherui.github.io/'
TIMEZONE = 'Asia/Shanghai'
#THEME = "tuxlite_tbs"
THEME = "bootlex"
DEFAULT_LANG = u'zh'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
GITHUB_URL = "https://github.com/lizherui"
GOOGLE_ANALYTICS = "UA-42648273-1"
DISQUS_SITENAME = "lizherui"
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
ARCHIVES_URL = "archives.html"
#RELATIVE_URLS = True
DEFAULT_PAGINATION = 5

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          )

# Social widget
SOCIAL = (('rss', 'http://lizherui.github.io/feeds/all.rss.xml'),
          ('github', 'https://github.com/lizherui'),
          ('weibo', 'http://weibo.com/lzrm4a1'),
          ('zhihu', 'http://www.zhihu.com/people/li-zhe-rui'),
          ('twitter', 'https://twitter.com/lzrak47'),
          )

ARTICLE_URL = ('{slug}/')
ARTICLE_SAVE_AS = ('{slug}.html')
PAGE_URL = ('{slug}/')
PAGE_SAVE_AS = ('{slug}.html')
AUTHOR_URL = ('author/{name}/')
TAG_URL = ('tag/{name}/')
