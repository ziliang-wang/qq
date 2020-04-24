# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QqProjectItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    title = scrapy.Field()
    singer = scrapy.Field()
    time = scrapy.Field()
