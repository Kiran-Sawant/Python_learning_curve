"""
This script is an example of a Scrapy CrawlSpider.
A CrawlSpider has the capability to collect hyper-links on a page, and explore the page of that link.
There are several rules to keep in mind for using CrawlSpiders.
allowed_domains: it is a list of domains that the Spider is allowed to scrape. ie. if the spider comes
across a link that is not included in the allowed_domain list it will not open it, eg: social media links on a page.
rules: rules attribute takes a tuple of Rule object, each Rule has certain parameters to define how a spider must 
crawl the web
Rule object: Rule takes several parameters to define a crawl, but 3 are basic ones; A LinkExtractor() method,
callback function and follow boolean.
A LinkExtractor() method defines which links to extract from the page, here it will extract all the links. However, it will 
explore only the ones that belong to domain in allowed_domain.
callback:str takes a string representing the name of function that will extract the necessary information from the response.
follow:bool takes a boolean, if true; it will extract links from the page that was explored through the link that was given
by the LinkExractor, and try to extract the links that satisfy the LinkExtractor condition in the following page.

Spider starts scraping from the start_url, it sends a request to that URL and passes a scrapy.Response object to parse_item.
The parse_item() method parses the response body, gets the necessary data and yields a dictionary of useful information.
spider than grabs a hyper-link from the start_url that satisfies LinkExtractor() condition, sends a request to that link and
passes a Response object to the parse_item. If it finds a link satisfying the LinkExtractor() method on that page; it will
send a request to that page as well, to avoid such behaviour, set an appropriate condition in LinkExtractor(), or set follow=False"""

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time


class H1SpiderSpider(CrawlSpider):
    name = 'h1_spider'
    allowed_domains = ['books.toscrape.com']    # spider will crawl within this domain.
    start_urls = ['http://books.toscrape.com']  # spider will start here.

    # Rules determine what links are followed
    rules = (
        Rule(LinkExtractor(), 
        callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        
        items = response.xpath('//h1/text()').getall()

        for item in items:
            yield{
                'text': item,
                'url': response.url
            }
        time.sleep(1)
