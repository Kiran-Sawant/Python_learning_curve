#%%
import re

string = "24th Jan 2004 26th Jan 1950"

#%% Creating named groups regex
day_regex   = r"(?P<day>\d+(?=th))"
month_regex = r"(?P<month>\s\w+\s)"
year_regex  = r"(?P<year>\d{2,4}$)"

re.findall(day_regex, string)
# %%
grp = re.search(day_regex, string)
print(grp)
# %%
for i in re.finditer(day_regex, string):
    print(i['day'])

# %%
