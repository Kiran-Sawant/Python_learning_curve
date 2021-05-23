import scrapy


class Quotes2Spider(scrapy.Spider):
    name = 'quotes2'
    # allowed_domains = ['https://quotes.toscrape.com/']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        
        quotes = response.css(".quote")
        for quote in quotes:
            item = {
                'author': quote.css('.author::text').get(),
                'quote': quote.css('.text::text').get(),
                'tags': quote.css('.tag::text').getall()
            }
        
            yield item
