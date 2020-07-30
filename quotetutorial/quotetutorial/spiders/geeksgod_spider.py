import scrapy
from ..items import QuotetutorialItem
class QuoteSpider(scrapy.Spider):
    name = 'geeksgod'
    start_urls = ['https://geeksgod.com/category/freecoupons/udemy-courses-free/'
    ]
    def parse(self,response):
        link=response.css(".td-module-title a::attr(href)").extract()
        lastdate=response.css(".td-post-date time::text").extract()
        yield { "link" : link,
                "lastdate" : lastdate
              }
