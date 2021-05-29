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
        return body

if __name__ == "__main__":
    url = "https://www.spoonflower.com/en/shop?on=fabric"

    results = asyncio.run(scraper(url))
