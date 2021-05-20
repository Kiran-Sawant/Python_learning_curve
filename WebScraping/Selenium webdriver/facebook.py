import getpass
import time
import os
from urllib.parse import urlparse

import requests
from selenium import webdriver

from conf import (FB_USERNAME, FB_PASSWORD)

def click_to_follow(browser: webdriver)->None:

    my_button_xpath = "//*[contains(text(), 'Follow')] [not(contains(text(), 'Following'))] [not(contains(text(), 'Followers'))]"
    follow_btn_elements = browser.find_elements_by_xpath(my_button_xpath)

    print(follow_btn_elements)

    for btn in follow_btn_elements:
        time.sleep(2)
        try:
            btn.click()
        except:
            pass

browser = webdriver.Chrome()
url = "https://www.fb.com"

time.sleep(1)
browser.get(url)

email_el = browser.find_element_by_name('email')
email_el.send_keys(FB_USERNAME)

time.sleep(2)

password_el = browser.find_element_by_name('pass')
password_el.send_keys(FB_PASSWORD)

time.sleep(3)
password_el.submit()

time.sleep(10)
mark_url = "https://www.facebook.com/Markmansonnet"
browser.get(mark_url)

click_to_follow(browser)

time.sleep(10*60)
browser.close()

# xpath.
my_button_xpath = "//button"
browser.find_elements_by_xpath(my_button_xpath)

# getting the follow buttons and not following buttons.
# my_button_xpath = "//button[contains(text(), 'Follow')] [not(contains(text(), 'Following'))]"
# follow_btn_elements = browser.find_elements_by_xpath(my_button_xpath)
# my_button_xpath = "//a[contains(text(), 'Follow')] [not(contains(text(), 'Following'))]"
# follow_btn_elements = browser.find_elements_by_xpath(my_button_xpath)

# get all img tag elements
image_elms = browser.find_elements_by_xpath("//img")
# get all video tag elements
video_elms = browser.find_elements_by_xpath("//video")

# settingup directories to save files
base_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(base_dir, 'Images')

# making the directory
os.makedirs(img_dir, exist_ok=True)

for img in image_elms:
    # print(img.get_attribute('src'))         # getting the source of image
    img_path = img.get_attribute('src')
    base_img_path = urlparse(img_path).path
    filename = os.path.basename(base_img_path)
    with requests.get(img_path, stream=True) as r:
        # if error with request continue with next iteration
        try:
            r.raise_for_status()
        except:
            continue
        
        with open(img_dir+filename, mode='wb') as f:
            for chunk in r.iter_content():
                if chunk:
                    f.write(chunk)

# function way

# making directory for downloaded data.
data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

def scrape_and_save(elements):
    for element in elements:
        # print(img.get_attribute('src'))         # getting the source of image
        img_path = element.get_attribute('src')
        base_img_path = urlparse(img_path).path
        filename = os.path.basename(base_img_path)
        filepath = os.path.join(data_dir, filename)

        if os.path.exists(filepath):    # if the file already exists.
            continue                    # break loop and move to next element.

        # requesting the image in the img tag
        with requests.get(base_img_path, stream=True) as r:
            # if error with request continue with next iteration
            try:
                r.raise_for_status()
            except:
                continue
            
            with open(img_dir+filename, mode='wb') as f:
                for chunk in r.iter_content(chunk_size=8000):
                    if chunk:
                        f.write(chunk)

scrape_and_save(image_elms)
scrape_and_save(video_elms)

"""
LONG TERM Goal:-
Use machine learning to classify the post
image or video
and then comment in a relevent fashion.
""" 

comment_xpath = "//textarea[contains(@placeholder, 'Add a comment')]"
comment_elm = browser.find_element_by_xpath(comment_xpath)
comment_elm.send_keys("Awsome!")

submit_btn_elms = browser.find_elements_by_css_selector("button[type='submit']")

for btn in submit_btn_elms:
    try:
        btn.click()
    except:
        continue

# wraping automated comments in function
def auto_comment(browser: webdriver, content: str='Hello'):
    comment_box_xpath = "//textarea[contains(@placeholder, 'Add a comment')]"
    comment_elm = browser.find_element_by_xpath(comment_box_xpath)
    comment_elm.send_keys(content)

    submit_btn_elms = browser.find_elements_by_css_selector("button[type='submit']")

    for btn in submit_btn_elms:
        try:
            btn.click()
        except:
            continue

auto_comment(browser, content='A chomo!')