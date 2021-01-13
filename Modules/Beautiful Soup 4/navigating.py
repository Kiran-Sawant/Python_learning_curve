import bs4 as bs
import urllib.request as request

sauce = request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# Creating a new soup object of the contants in <nav> tag
nav = soup.nav

# grabbing hyperlinks in the nav bar.
for link in nav.find_all('a'):
    print(link.get('href'))         # .get(attr) returns the value of that attribute.

#________Grabbing specific tags__________#
"""Sometimes there might be multiple tags with the same names, but different attributes,
and you might want to grab information from a specific tag with a specific attribute.
For example, the page that we're working with has a div tag with the class of 'body'
use attrs parameter to specify attributes & their values."""
for div in soup.find_all('div', attrs={'class': 'body'}):
    print(div.text)