import bs4 as bs
import urllib.request as request

sauce = request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# get entire title tag of the page.
print(soup.title)

# get attributes of title.
print(soup.title.name)

# get value in the title tag.
print(soup.title.string)

# getting contents in the head, parent tag of title tag.
print(soup.title.parent)

#_________ .find_all('tag') method___________#
"""Returns a list of tag contents with the tag of the tag that is passed."""
# getting a list of all paragraph tags
paras = soup.find_all('p')

for para in paras:
    print(para)               # prints with tags.
    print(para.string)        # prints values if no child tags.
    print(str(para.text))     # prints all texts.

for url in soup.find_all(name='a'):
    print(url.text)               # text to get content between the tag
    print(url.get('href'))        # .get() method can be used to get the attributes of a tag.
    print(url.get('class'))       # getting class attribute of <a> tag.
 