""" re.findall() creates a list of strings that matched the passed
regular expression."""

import re

example = """
Killer Bean is 50, Ronald McDonald is 44, King George is 778"""

# Retriving names
"""Creating reguler expression for full name:
first charecter between A to Z followed by 0 or more charecters
between a to z, followed by space, followed by a charecter between
A to Z, followed by 0 or more any charecters."""

names = re.findall(r"[A-Z][a-z]*\s[A-Z]\w*", example)

"""Creatin regular expression for age:
any 1 to 3 number """
ages = re.findall(r"\d{1,3}", example)

print(names)
print(ages)