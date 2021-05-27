import scrapy


class ParisSpider(scrapy.Spider):
    name = 'paris'
    # allowed_domains = ['x.com']
    start_urls = ['https://en.wikipedia.org/wiki/Eiffel_Tower']

    def parse(self, response):
        raw_img_urls = response.css(".image img::attr(src)").getall()   # relative URLs
        clean_img_urls  = []                                            # absolute URLs

        '''response.urljoin(r_url) returns an absolute URL, 
        based on the URL to which the request was sent.'''
        for img_url in raw_img_urls:
            clean_img_urls.append(response.urljoin(img_url))

        #__________test____________#
        # for url in clean_img_urls:
        #     print(url)

        yield {
            'image_urls': clean_img_urls
        }