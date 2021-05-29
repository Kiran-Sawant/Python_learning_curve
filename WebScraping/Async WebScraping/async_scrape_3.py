# This module adds DataFrame conversion and saving to pickle over async_scrape_2.py
import os
import asyncio
import itertools
import re
import time
import pathlib

import pandas as pd
from arsenic import (get_session, keys, browsers, services)
from requests_html import HTML


async def extract_id_slug(url_path: str):
    """separates product id and product slug, from product link."""

    regex = r"^[^\s]+/(?P<id>\d+)-(?P<slug>[\w_-]+)$"
    group = re.match(regex, url_path)
    if not group:
        return (None, None)
    return (group['id'], group['slug'])

async def get_fabric_links(html_body: str)->list:
    """Returns a list of dictionaries, each dictionary contains  
    product id, slug and link.
    attr:
        html_body(str): body of an HTML page as string."""

    html_r = HTML(html=html_body)
    fabric_links = list(x for x in html_r.links if '/fabric/' in x)
    datas = list()

    #_________test____________#
    # for link in fabric_links:
    #     print(link)

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

async def scraper(url: str)->str:
    """Scrapes the HTML of the passed URL using arsenic webdriver."""

    service = services.Chromedriver()
    browser = browsers.Chrome()
    browser.capabilities = {
        'goog:chromeOptions': {'args': ['--headless', '--disable-gpu']}
    }

    # creating an arsenic session and running it inside of a context manager.
    async with get_session(service, browser) as session:
        await session.get(url)
        body = await session.get_page_source()
        return body

async def store_links_as_df_pickle(datas:list, name:str='links.pkl')->pd.DataFrame:
    """Takes a list of dictionaries and returns a pandas DataFrame"""

    df = pd.DataFrame(datas)
    df.set_index('id', inplace=True)
    df.to_pickle(name)
    return df

async def run(url: str):
    """A manager function for a set of async functions."""

    body_content = await scraper(url)
    links = await get_fabric_links(body_content)
    df = await store_links_as_df_pickle(links)
    return df


if __name__ == "__main__":
    url = "https://www.spoonflower.com/en/shop?on=fabric"

    # to run an async function without using await, use asyncio.run()
    df = asyncio.run(run(url))
    print(df)
