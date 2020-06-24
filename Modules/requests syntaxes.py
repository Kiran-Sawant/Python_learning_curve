import requests

# r = requests.get('https://imgs.xkcd.com/comics/python.png')

# print(r.status_code)            # Gives http status codes
# print(r.ok)                     # True if ok & False if http error
# print(r.headers)

# writing to file.
# with open("comic.png", mode='wb') as f:
#     f.write(r.content)

# http get method_____________________#
payload = {'page': 2, 'count': 25}
k = requests.get('https://httpbin.org/get', params=payload)

# print(k.url)

# http post method____________________#
payload = {'username': 'Corey', 'password': 'testing'}
j = requests.post('https://httpbin.org/post', data=payload)

# print(j.json())