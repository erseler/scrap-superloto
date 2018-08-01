# -*- coding: utf-8 -*-

# Scrapy settings for superloto project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'superloto'

SPIDER_MODULES = ['superloto.spiders']
NEWSPIDER_MODULE = 'superloto.spiders'

ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 0.5
HTTPCACHE_ENABLED = True
