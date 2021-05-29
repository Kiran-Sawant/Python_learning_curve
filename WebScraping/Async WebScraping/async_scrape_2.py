# This module adds manager function and separating id, slug from links.
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

async def get_fabric_links(html_body: str):
    """Returns a list of dictionaries, each dictionary contains  
    product id, slug and link.
    attr:
        html_body(str): body of an HTML page as string."""

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

async def scraper(url: str):
    """Returns the HTML of the passed URL using arsenic webdriver."""

    service = services.Chromedriver()
    browser = browsers.Chrome()
    browser.capabilities = {
        'goog:chromeOptions': {'args': ['--headless', '--disable-gpu']}
    }

    # creating an arsenic session and running it inside of a context manager.
    async with get_session(service, browser) as session:
        await session.get(url)
        body = await session.get_page_source()
        pritn(body)
        return body

async def run(url: str):
    body_content = await scraper(url)
    links = await get_fabric_links(body_content)

    return links


if __name__ == "__main__":
    url = "https://www.spoonflower.com/en/shop?on=fabric"

    results = asyncio.run(run(url))
