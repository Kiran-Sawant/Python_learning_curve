#%%
"""
This module opens chrome browser visit duckduckgo.com and searches for 
SpongeBob Square pants (line-20), navigates to images tab, and downloads
images that appear first, without scroll auto load (100 approx)."""

import time
from pathlib import Path
from urllib.parse import urlparse

import requests
from selenium import webdriver

#%% Opening browser
browser = webdriver.Chrome()

# %% visiting duckduckgo.com
url = "https://www.duckduckgo.com"
browser.get(url)

# %% inserting query in search box and submit
search_box = browser.find_element_by_name('q')
search_box.clear()
search_box.send_keys("SpongeBob Square pants")
search_box.submit()

# %% clicking images tab
images_btn_path = "//a[contains(text(), 'Images')]"
images_btn = browser.find_element_by_xpath(images_btn_path)
images_btn.click()

# %% seleting large quality images
# droping down size tab.
size_drop = browser.find_element_by_class_name("dropdown--size")
size_drop.click()

# clicking large size button.
large_img_path = "//a[contains(@data-value, 'Large')]"
large_img_btn = browser.find_element_by_xpath(large_img_path)
large_img_btn.click()

# %% getting all image tiles on image page
image_tiles = browser.find_elements_by_class_name('tile--img__media')
len(image_tiles)

# %% Looping through each tile detail and downloading images.
for tile in image_tiles:
    tile.click()

    time.sleep(2)

    view_file_btn_path = "//a[contains(text(), 'View File')]"       # x-path for view image button on dd-go
    view_file = browser.find_element_by_xpath(view_file_btn_path)   # getting the button
    og_img_src = view_file.get_attribute('href')                    # grabbing og img link from btn
    base_img = urlparse(og_img_src).path                            # getting rid of URL parameters if any
    base_img_name = base_img.split('/')[-1]                         # getting the image name

    #______setting up download directory______#
    project_dir = Path(__file__).parent                             # getting the path of this project in OS.
    img_dir_path = project_dir.joinpath("Downloaded_data")          # creating a path to download directory.
    img_dir_path.mkdir(exist_ok=True)                               # creating empty directory if doesn't exists
    
    file_path = img_dir_path.joinpath(base_img_name)                # creating full image file path preemtively

    if file_path.exists():                                          # if the file is already saved (based on file name)
        continue

    with requests.get(og_img_src, stream=True) as r:                # sending a request to original image link
        try:
            r.raise_for_status()
        except:
            pass

        with open(file_path, mode='wb') as file_:
            for chunk in r.iter_content(chunk_size=8000):
                file_.write(chunk)                                  # saving the image downloaded from request

# %%

