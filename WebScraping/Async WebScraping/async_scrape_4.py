# added code to add to previously saved DataFrames
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

async def scraper(url: str)->str:
    """Scrapes the HTML of the passed URL using arsenic webdriver."""

    service = services.Chromedriver()
    browser = browsers.Chrome()
    browser.capabilities = {
        'goog:chromeOptions': {'args': ['--headless', '--disable-gpu']}
    }

    async with get_session(service, browser) as session:
        await session.get(url)
        body = await session.get_page_source()
        return body

def store_links_as_df_pickle(datas:list, path:str='links.pkl')->pd.DataFrame:

    new_df = pd.DataFrame(datas)                        # creatign a DataFrame out of passed list

    if pathlib.Path(path).exists():                     # if a previous dataframe pickle exists.
        og_df = pd.read_pickle(path)                    # get previous df
        df = pd.concat([og_df, new_df], sort=False)     # concatinate old & new df
        df.drop_duplicates(subset=['id'], inplace=True) # droping rows with same product id, avoid duplication.
        df.to_pickle(path)
        return df
    else:                                               # if no previously saved df found
        new_df.to_pickle(path)
        return new_df

async def run(url: str)->None:
    body_content = await scraper(url)
    links = await get_fabric_links(body_content)
    df = store_links_as_df_pickle(links)
    return df


if __name__ == "__main__":
    url = "https://www.spoonflower.com/en/shop?on=fabric"

    df = asyncio.run(run(url))
    print(df.shape)
