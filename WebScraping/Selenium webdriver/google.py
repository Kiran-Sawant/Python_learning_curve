import time

from selenium import webdriver

browser = webdriver.Chrome()

url = 'https://www.google.com/'

time.sleep(1)
browser.get(url)

name = 'q'

search_el = browser.find_element_by_name(name)

time.sleep(2)
search_el.send_keys("sex")

time.sleep(1)
search_el.submit()