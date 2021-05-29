# Recording time.
import os
import asyncio
import itertools
import re
import time
import pathlib

import pandas as pd
from arsenic import (get_session, keys, browsers, services)
from requests_html import HTML

def store_links_as_df_pickle(datas:list, path:str='links.pkl')-> pd.DataFrame:

    new_df = pd.DataFrame(datas, index='id')

    if pathlib.Path(path).exists():                     # if a previous dataframe pickle exists.
        og_df = pd.read_pickle(path)                    # get previous df
        df = pd.concat([og_df, new_df], sort=False)     # concatinate old & new df
        df.drop_duplicates(subset=['id'], inplace=True) # droping rows with same product id, avoid duplication.
        df.to_pickle(path)
        return df
    else:    
        new_df.to_pickle(path)
        return new_df

async def extract_id_slug(url_path: str)-> tuple:
    """separates product id and product slug, from product link."""

    regex = r"^[^\s]+/(?P<id>\d+)-(?P<slug>[\w_-]+)$"
    group = re.match(regex, url_path)
    if not group:
        return (None, None)
    return (group['id'], group['slug'])

async def get_fabric_links(html_body: str)-> list:

    html_r = HTML(html=html_body)
    fabric_links = list(x for x in html_r.links if '/en/fabric' in x)
    datas = list()

    for link in fabric_links:
        id_, slug_ = await extract_id_slug(link)
        data = {
            'id': id_,
            'slug': slug_,
            'path': link,
            'scraped': 0
        }
        datas.append(data)

    return datas

async def scraper(url:str, i=-1, timeout:int=60, start=None)-> list:
    """Scrapes the HTML of the passed URL using arsenic webdriver.
    Returns a list of dictionaries, with product id, slug, link."""

    service = services.Chromedriver()
    browser = browsers.Chrome()
    browser.capabilities = {
        'goog:chromeOptions': {'args': ['--headless', '--disable-gpu']}
    }

    async with get_session(service, browser) as session:
        # if the page doesn't respond, return an empty URLs list.
        try:
            await asyncio.wait_for(session.get(url), timeout=timeout)
        except asyncio.TimeoutError:
            return []

        body = await session.get_page_source()
        links = await get_fabric_links(body)

        if start is not None:
            end = time.time() - start
            print(f"{i} took {end} seconds")

        return links

async def run(urls:list, timeout:int=60, start=None)->list:
    """
    attr:
        urls(list): list of URLs of webpages to scrape.
        timeout(int): timeout for async."""

    site_links = list()
    # df = store_links_as_df_pickle(links)

    for i, url in enumerate(urls):
        site_links.append(
            asyncio.create_task(scraper(url, i=i, start=start))
        )
    
    list_of_links = await asyncio.gather(*site_links)
    return list_of_links


if __name__ == "__main__":
    urls = ["https://www.spoonflower.com/en/shop?on=fabric&page_offset=1",
            "https://www.spoonflower.com/en/shop?on=fabric&page_offset=2",
            "https://www.spoonflower.com/en/shop?on=fabric&page_offset=3",]

    start = time.time()
    results = asyncio.run(run(urls, timeout=30, start=start))
    end = time.time() - start
    print(f"Total time is {end}")
    print(f"length of site_links list: {len(results)}")

