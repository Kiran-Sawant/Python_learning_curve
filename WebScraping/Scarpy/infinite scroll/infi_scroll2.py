# Upen's code
"""This script scrapes quotes from toscrpe.com and yields them as a dictionary."""

import scrapy


base = "https://quotes.toscrape.com/api/quotes?page={}"

class InfiScroll2Spider(scrapy.Spider):
    name        = 'infi_scroll2'
    start_urls  = [base.format(1)]

    def parse(self, response):
        data = response.json()

        # print(f"Has Next: {data['has_next']}")
        # print(f"Page No: {data['page']}")
        current_page = data['page']

        for quote in data['quotes']:
            yield {
                "author": quote['author']['name'],
                "quote" : quote['text']
            }
        
        if data['has_next']:
            next_page_url = base.format(current_page+1)
            yield scrapy.Request(next_page_url)

