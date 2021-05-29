# Scraping multiple URLs, i.e. multiple pages.
# run python -m supercharged.main spoonflower

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

from storage import store_links_as_df_pickle
from .projects.spoonflower import run_spoonflower


class Pipeline():
    
    def __init__(self, *args, **kwargs):
        self.spoonflower = run_spoonflower

if __name__ == "__main__":
    fire.Fire(Pipeline)
