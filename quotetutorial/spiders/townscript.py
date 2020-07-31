import scrapy
from ..items import QuotetutorialItem
class QuoteSpider(scrapy.Spider):
    name = 'townscript'
    start_urls = ['https://www.townscript.com/in/coimbatore/near-you?page=1','https://www.townscript.com/in/coimbatore/near-you?page=2'
    ]
    def parse(self,response):
        items = QuotetutorialItem()
        all_div_events=response.css("div.card-container")
        #for quotes in all_div_events:
        for event in all_div_events:
            eventname=event.css("div.event-name-box span::text").extract()
            eventdate=event.css("div.date span::text").extract()
            eventprice=event.css('div.price span::text').extract()
            items['eventname'] = eventname
            items['eventdate'] = eventdate
            items['eventprice'] = eventprice
            yield items
