"""A spider that scrapes a single quote from toscrape.com"""

import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['quotes.toscrape.com/random']
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        # print(f"Got response from: {response.url}")
        self.log(f"Got response from: {response.url}")

        item = {
            'author': response.css(".author::text").get(),
            'quote': response.css(".text::text").get(),
            'tags': response.css(".tag::text").getall()
        }

        yield item
