import re

#_____________String_____________#
text = '''abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

# Expression for selecting Men only.
^Mr[^s].\w+

# Expression to select women only
M(s|rs)\.?\s\w+'''

urls = '''https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov'''

sentence = 'Start a sentence and then bring it to an end.'

#___________re methods_____________#
"""Compile a regular expression pattern into a Pattern object,
which can be used for matching using its match(), search() and other
methods, described below."""
pattern = re.compile(r'\bHa')

#_______ .finditer() method________#
"""Creates an iterable containing Match object.
Each Match object contains info of string matching with Pattern."""
matches = pattern.finditer(text)

for match in matches:
    print(match)

#__________ re.split() method___________#
"""Split string by the occurrences of Pattern."""
split_ = re.split(r"\s", "Hay You Yes You!")
print(f"split method: {split_}")

#____________ re.escape() method_____________#
'''Escape special characters in pattern.'''
escape_ = re.escape(r"killer\nBean\tForever")
print(f"Escape: {escape_}")

#___________working with Match.group()___________#
# Compiling RegEx
pattern_2 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# creating iterable
matches_2 = pattern_2.finditer(urls)

for match in matches_2:
    # printing domain name ie. second group.
    print(match.group(2))

#___________Substitution method__________#
"""Keeps the groups mentioned in the raw string and removes rest."""
# keeping only 2nd & 3rd group mentioned in Pattern.
subbed_urls = pattern_2.sub(r'\2\3', urls)
print(subbed_urls)

#____________match method_____________#
"""If zero or more characters at the beginning of string match the regular
expression pattern, return a corresponding match object. Return None if
the string does not match the pattern."""
pattern_3 = re.compile(r'Davis')
matches_3 = pattern_3.match(text)
print(matches_3)

#____________search method_____________#
'''Scan through string looking for the first location where the regular expression
pattern produces a match, and return a corresponding match object.'''
matches_4 = pattern_3.search(text)
print(matches_4)
