# Scraping multiple URLs, i.e. multiple pages.

import os
import asyncio
import itertools
import re
import time
import pathlib
from urllib.parse import urlparse

import fire
from arsenic import (get_session, keys, browsers, services)
from requests_html import HTML

from ..scrapers import scraper
from ..log_handler import set_arsenic_log_level
from ..storage import (store_links_as_df_pickle, list_to_sql)

async def extract_id_slug(url_path:str)-> tuple:
    """separates product id and product slug, from product link."""

    parsed_url  = urlparse(url_path)
    path        = parsed_url.path
    regex = r"^[^\s]+/(?P<id>\d+)-(?P<slug>[\w_-]+)$"
    group = re.match(regex, url_path)
    if not group:
        return (None, None, path)
    return (group['id'], group['slug'], path)

async def get_parsable_html(raw_html:str)->HTML:
    """Takes a raw HTML string and returns parsable
     requests_html.HTML object"""
     
    return HTML(html=raw_html)

async def get_fabric_links(html_r:HTML)-> list:
    """Get relative links of fabric detail page from an requests_html.HTML object"""

    fabric_links = list(x for x in html_r.links if '/en/fabric' in x)
    datas = list()

    for link in fabric_links:
        id_, slug_, _ = await extract_id_slug(link)
        data = {
            'id': id_,
            'slug': slug_,
            'path': link,
            'scraped': 0
        }
        datas.append(data)

    return datas

async def get_product_data(url:str, html_r:HTML)->dict:

    id_, slug_, path = await extract_id_slug(url)
    title_elm        = html_r.find(".design-title")
    size_elm         = html_r.find('#fabric-size')
    price_elm        = html_r.find(".visuallyhidden span")

    data = {
        'id': id_,
        'slug': slug_,
        'path': path,
    }

    if len(title_elm) > 0:
        #_________grabbing title_____________#
        title = title_elm[0].text
        #_________grabing size and dimension___________#
        sizes = re.findall(r"\d+(?=\s\w{1,2})", size_elm[0].text)
        length, breadth = int(sizes[0]), int(sizes[1])
        unit = re.findall(r"(?<=\d\d\s)\w+", size_elm[0].text)[0]
        #_____________Grabbing price data_____________#
        amount = price_elm[0].attrs['content']
        currency = price_elm[1].attrs['content']
        #____________inserting data____________#
        data['title']    = title
        data['length']   = length
        data['breadth']  = breadth
        data['unit']     = unit
        data['price']    = float(amount)
        data['currency'] = currency
    
    return data

async def spoonflower_scraper(url:str, i=-1, timeout:int=60, start=None)-> dict:
    """Scrapes the HTML of the passed URL using arsenic webdriver.
    Returns a list of dictionaries, with product id, slug, link."""
    body    = await scraper(url, timeout=timeout, delay=10)       # getting raw HTML
    html_r  = await get_parsable_html(body)         # converting to parsable HTML
    links   = await get_fabric_links(html_r)        # getting relative links
    product_data = await get_product_data(url, html_r)
        
    dataset = {
        "links": links,
        "product_data": product_data
    }
    #_____________printing time consumption_________________#
    if start is not None:
        end = time.time() - start
        print(f"{i} took {end} seconds")

    return dataset

async def run(urls:list, timeout:int=60, start=None)->list:
    """
    attr:
        urls(list): list of URLs of webpages to scrape.
        timeout(int): timeout for async."""

    site_links = list()
    # df = store_links_as_df_pickle(links)

    for i, url in enumerate(urls):
        site_links.append(
            asyncio.create_task(spoonflower_scraper(url, i=i, start=start))
        )
    
    list_of_links = await asyncio.gather(*site_links)
    return list_of_links



def run_spoonflower():
    start = time.time()
    urls = ["https://www.spoonflower.com/en/shop?on=fabric",
            "https://www.spoonflower.com/en/fabric/6075822-soft-meadow-floral-by-sweeterthanhoney",]

    results = asyncio.run(run(urls, timeout=30, start=start))
    print(results)
    end = time.time() - start
    print(f"Total time taken: {end}")

    links = [x['links'] for x in results]           # list of lists containing links
    links = itertools.chain.from_iterable(links)
    links = list(links)                             # list of links

    # df = store_links_as_df_pickle(results, path='links.pkl')
    # df = asyncio.run(run(url))
    # print(f"length of site_links list: {len(results)}")

    list_to_sql(links, table_name='spoonflower_links')

    product_data = [x['product_data'] for x in results]     # list of dictionaries
    list_to_sql(product_data, table_name='spoonflower_fabrics')

    return results

# if __name__ == "__main__":
#     fire.Fire(Pipeline)
