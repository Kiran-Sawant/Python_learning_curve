import asyncio
from arsenic import (services, browsers, get_session)

async def scraper(url:str, i=-1, timeout:int=60, delay:int=10)-> dict:
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
            await asyncio.wait_for(session.get(url), timeout=60)
        except asyncio.TimeoutError:
            return []

        if delay > 0:
            await asyncio.sleep(10)
        body    = await session.get_page_source()       # getting raw HTML

        return body