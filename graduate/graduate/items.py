# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GraduateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class InvestmentItem(scrapy.Item):
    title = scrapy.Field()                     #标题
    date = scrapy.Field()                      #日期
    content = scrapy.Field()                   #内容
    source = scrapy.Field()                    #来源
    link = scrapy.Field()                      #链接