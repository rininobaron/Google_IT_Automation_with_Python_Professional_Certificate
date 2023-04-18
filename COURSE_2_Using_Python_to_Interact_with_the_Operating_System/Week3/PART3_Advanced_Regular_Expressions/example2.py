#! /usr/bin/env python3

import re

print("Search for letters repeated five times")
lines=["a ghost", " a scary ghost appeared"]
for line in lines:
	print(line)
	print(re.search(r"[a-zA-Z]{5}", line))
print()

print("Search for letters repeated five times (more matches)")
for line in lines:
	print(line)
	print(re.findall(r"[a-zA-Z]{5}", line))
print()

print("Search for letters repeated exactly five times (more matches)")
for line in lines:
	print(line)
	print(re.findall(r"\b[a-zA-Z]{5}\b", line))
print()

print("Search for alfanumeric characters repeated five to ten times (more matches)")
line="I really like strawberries"
print(line)
print(re.findall(r"\w{5,10}", line))
print()

print("Search for alfanumeric characters repeated at least five times (more matches)")
print(line)
print(re.findall(r"\w{5,}", line))
print()

print("Search for word started with s and follow by up to \
	20 alfanumeric characters")
print(line)
print(re.search(r"s\w{,20}", line))
print()

print("Exercise!")
def long_words(text):
	pattern = r"\w{7,}"
	result = re.findall(pattern, text)
	return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []







