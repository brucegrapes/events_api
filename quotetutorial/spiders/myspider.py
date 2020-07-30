import scrapy
from ..items import QuotetutorialItem
class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://www.townscript.com/in/coimbatore'
    ]
    def parse(self,response):
        items = QuotetutorialItem()
        all_div_events=response.css('div.card-body')
        #for quotes in all_div_events:
        for event in all_div_events:
            eventname=event.css("div.event-name span::text").extract()
            eventdate=event.css("div.date ::text").extract()
            eventprice=event.css('div.price span::text').extract()
            items['eventname'] = eventname
            items['eventdate'] = eventdate
            items['eventprice'] = eventprice
            yield items
