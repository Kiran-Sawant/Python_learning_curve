"""Getting all the links from the sitemap.
sitemap links to an XML file."""

import bs4 as bs
import urllib.request as request

# getting the XML page
data = request.urlopen(r'https://pythonprogramming.net/sitemap.xml').read()

# Creating a soup object using xml parser.
xml_soupe = bs.BeautifulSoup(data, 'xml')

locs = xml_soupe.find_all('loc')

for i in locs:
    print(i.text)