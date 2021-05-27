"""Scraping Dynamically loaded site"""

import scrapy
import json

class NtschoolsSpider(scrapy.Spider):
    name = 'ntschools'
    # allowed_domains = ['s']
    start_urls = ['https://directory.ntschools.net/#/schools']

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': 1,
        'Host': 'directory.ntschools.net',
        'Referer': 'https://directory.ntschools.net/',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    }

    def parse(self, response):
        """Creates a Request object from the given REST api URL.
        Yields one Response object at a time."""

        url = 'https://directory.ntschools.net/api/System/GetAllSchools'

        response = scrapy.Request(url,
            callback=self.parse_api,
            headers=self.headers)
        
        yield response

    def parse_api(self, response):
        """Creates URL for detail of a single school,
        yields a response for an API call made for detail of a single school."""

        # base URL for getting school detail.
        base_url = "https://directory.ntschools.net/api/System/GetSchool?itSchoolCode="

        # JSON string received from REST API call.
        raw_data = response.body
        # Converting JSON string to dictionary.
        data = json.loads(raw_data)

        for school in data:
            school_code = school['itSchoolCode']        # code of individual school
            school_url = base_url + school_code         # API end-point for details of a single school.
            response = scrapy.Request(school_url,
                callback=self.parse_school,
                headers=self.headers)
            
            yield response
    
    def parse_school(self, response):

        raw_data = response.body
        data = json.loads(raw_data)

        yield {
            "Name": data['name'],
            "PhysicalAddress": data['physicalAddress']['displayAddress'],
            "PostalAddress": data['postalAddress']['displayAddress'],
            "Email": data['mail'],
            "Phone": data['telephoneNumber']
        }