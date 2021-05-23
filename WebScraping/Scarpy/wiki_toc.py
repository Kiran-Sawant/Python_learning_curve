"""A spider that scrapes table of content from wikipedia pages."""

import scrapy


class WikiTocSpider(scrapy.Spider):
    name = 'wiki_toc'
    # allowed_domains = ['en.wikipedia.org/wiki/Python_(programming_language)']
    start_urls = ['https://en.wikipedia.org/wiki/Python_(programming_language)']

    def parse(self, response):
        
        self.log(f"Got response  from: {response.url}")

        sr_no = list(float(x) for x in response.css(".tocnumber::text").getall())
        content = response.css(".toctext::text").getall()
        toc = dict(zip(sr_no, content))
        # print(toc)
        yield toc
