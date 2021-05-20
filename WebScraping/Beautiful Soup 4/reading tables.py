import bs4 as bs
import urllib.request as request
import pandas as pd

# Getting raw HTMN
sauce = request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()

# Soup of entire page.
soup = bs.BeautifulSoup(sauce, 'lxml')

# Soup of table.
table = soup.find('table')
# Soup of table rows.
table_rows = table.find_all('tr')

my_list = list()

# getting table row data
for tr in table_rows:
    td = tr.find_all('td')          # Getting a list of <td> tags.
    row = [x.text for x in td]      # Getting text between <td> tag.
    # print(row)
    my_list.append(row)


df = pd.DataFrame(my_list, columns=['Program name', 'Internet Points', 'Kittens'])
# print(df)

#_________Pandas way____________#
# Returns a list of DataFrames of all tables in the Web page.
tab = pd.read_html("https://pythonprogramming.net/parsememcparseface/", header=0)
print(tab[0])