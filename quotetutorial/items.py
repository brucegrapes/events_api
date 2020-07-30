# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    eventname= scrapy.Field()
    eventdate= scrapy.Field()
    eventprice= scrapy.Field()
    pass
