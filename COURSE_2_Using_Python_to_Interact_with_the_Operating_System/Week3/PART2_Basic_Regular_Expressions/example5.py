#! /usr/bin/env python3

import re

print("Search for pattern A.*a")
countries=["Argentina","Azerbaijan","Australia"]
for country in countries:
	print(country)
	print(re.search(r"A.*a", country))
print()

print("Search for only words with beginning eith 'A' and ending with 'a'")
for country in countries:
	print(country)
	print(re.search(r"^A.*a$", country))
print()

print("Search for lines using pattern ^[a-zA-Z_][a-zA-Z0-9_]*$")
pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$"
lines=["_this_is_a_valid_variable_name", \
"this isn't a valid variable", \
"my_variable1", \
"2my_variable1"]
for line in lines:
	print(line)
	print(re.search(pattern, line))
print()

print("Exercise!")
def check_sentence(text):
	result = re.search(r"^[A-Z][a-z| ].*[.|?|!]$", text)
	return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
print()