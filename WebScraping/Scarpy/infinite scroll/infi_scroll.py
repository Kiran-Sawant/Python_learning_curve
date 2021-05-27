# Failed code

import scrapy
import json

base = "https://quotes.toscrape.com/api/quotes?page={}"

class InfiScrollSpider(scrapy.Spider):
    name = 'infi_scroll'
    # allowed_domains = ['x']
    start_urls = [base.format(1)]

    http_headers = {
        'Host': 'quotes.toscrape.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://quotes.toscrape.com/scroll',
        'Cookie': 'session=eyJjc3JmX3Rva2VuIjoiREhqRllrZk9oY3pVTUpxWG9nSU5wR1J2ckxRbG5zdEJFaUttWmJXVnlUYVN1Q0FkZXd4UCJ9.YKyaSw.pF1mVV-6EuijI4uu0QvhQcqPEGA',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers'
    }
    
    def parse(self, response):

        base_url    = "https://quotes.toscrape.com/api/quotes?page={}"
        raw_data    = response.body             # JSON STRING
        data        = json.loads(raw_data)      # dictionary
        # print('#'*10+f"---Page number: {data['page']}---"+'#'*10)
        page_no = data['page']
        print(data['quotes'])
        yield {
            "author": data['quotes'][0]['author']['name']
        }

        if data['has_next'] == True:
            print("it is TRUEeeeeee")

            scrapy.Request(base_url.format(page_no + 1))
        
            
