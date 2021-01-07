import json
from urllib.request import urlopen
import urllib

while True:
    base = input("Insert base currency: ").upper().strip(' ')
    try:
        link = f"https://api.exchangeratesapi.io/latest?base={base}"
        break
    except urllib.error.HTTPError:
        print('Try a valid currency Abbriviation.')

with urlopen(link) as response:
    source = response.read()

data = json.loads(source)

for rate in data['rates']:
    print(f"{rate}: {data['rates'][rate]:.3f}")