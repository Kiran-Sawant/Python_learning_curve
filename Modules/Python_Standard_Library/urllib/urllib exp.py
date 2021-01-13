import urllib.request as u_request
import urllib.parse as u_parse

# Opening a URL
x = u_request.urlopen(r'https://www.google.com/search?q=nikki%20Lauda!')

# Reading the returned content of the URL
response = x.read()

#_______working with HTTP tags______#
url = 'http://duckduckgo.com'

# tag q is for query in duckduckgo.
values = {'q': 'KKR'}

# encoding tags in UTF-8 format.
data = u_parse.urlencode(values).encode('utf-8')
# Creating http request.
req = u_request.Request(url, data)
# sending request & saving response.
resp = u_request.urlopen(req)
# saving response in txt format
resp_data = resp.read()
# printingg response
print(resp_data)


# Some websites do not allow scripts to access their websites.
try:
    x = u_request.urlopen('https://www.google.com/search?q=Lauda!')

    print(x.read())
except Exception as e:
    print(str(e))

# bypassing Google's restriction for Scripts(Robots).
try:
    url = 'http://www.google.com/search?q=SalmanKhan'

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686)'
    req = u_request.Request(url, headers=headers)
    resp = u_request.urlopen(req)
    resp_data = resp.read()

    saveFile = open(__file__.replace('urllib exp.py', 'Headers.txt'), 'w')
    saveFile.write(str(resp_data))
    saveFile.close()

except Exception as e:
    print(str(e))
