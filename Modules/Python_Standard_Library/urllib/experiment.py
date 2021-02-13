from urllib import request
from urllib import parse


# k = request.urlopen('https://www.duckduckgo.com')

url = 'https://www.google.com'
tags = {'q': 'KKR'}
data = parse.urlencode(tags).encode('utf-8')
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686)'}
reqst = request.Request(url, headers=headers)

response = request.urlopen(reqst, data)

print(response.read())
# print(type(k))

# print(k.read())
