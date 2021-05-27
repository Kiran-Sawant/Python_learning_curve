import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksCrawlSpider(CrawlSpider):
    name = 'books_crawl'
    allowed_domains = ['books.toscrape.com/']
    start_urls = ['http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html']

    # Link extractors
    le_book_details = LinkExtractor(restrict_css='h3 > a')      # Extracting link of book detail page.
    le_next = LinkExtractor(restrict_css='.next > a')           # extracting link of next page in a paginated book list.

    # creating Rules
    rule_book_detail = Rule(le_book_details, 
                            callback='parse_item', 
                            follow=False)       # follow will not extract links from book detail page.
    rule_next_pg = Rule(le_next, follow=True)   # linkExtractor will extract links from next page.

    # passing Rule's
    rules = (
        rule_book_detail,
        rule_next_pg
    )

    def parse_item(self, response):
        
        yield{
            'Title': response.css('h1::text').get(),
            'Category': response.xpath("//ul[@class='breadcrumb']/li[last()-1]/a").get(),
            'Link': response.url
        }
