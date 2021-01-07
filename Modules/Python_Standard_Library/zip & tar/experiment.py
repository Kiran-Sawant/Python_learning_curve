import requests
import zipfile

r = requests.get("https://drive.google.com/open?id=1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV")

with open('data.zip', 'wb') as f:
    f.write(r.content)

with zipfile.ZipFile('data.zip', mode='r') as data_zip:
    print(data_zip.namelist())