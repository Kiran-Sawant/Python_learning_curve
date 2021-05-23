import scrapy
from bs4 import BeautifulSoup

class Exercise1Spider(scrapy.Spider):
    name = 'exercise1'
    # allowed_domains = ['scrapeit.home.blog']
    start_urls = ['http://scrapeit.home.blog/']

    def parse(self, response):
        
        articles = response.css("article")
        article_collection = []

        for article in articles:
            item = {
                "heading"  : article.css(".entry-header a::text").get(),
                "paragraph": BeautifulSoup(article.css(".entry-content p").get()).text,
                "author"   : article.css(".author a::text").get(),
                "date"     : article.css("time.entry-date::text").get(),
                "tags"     : article.css("a[rel='tag']::text").getall(),
                "category" : article.css("a[rel='category tag']::text").getall()
            }

            article_collection.append(item)

        return article_collection

