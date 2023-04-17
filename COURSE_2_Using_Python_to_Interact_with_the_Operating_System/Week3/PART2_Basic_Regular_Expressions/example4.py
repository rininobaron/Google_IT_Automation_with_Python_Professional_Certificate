#! /usr/bin/env python3

import re

print("Using '.'")
print(re.search(r".com", "welcome"))
print()

print(r"Using escape character '\' to ignore '.' to search '.com'")
words=["welcome","mydomain.com"]
for word in words:
	print(word)
	print(re.search(r"\.com", word))
print()

print(r"Using '\w' in order to search any alfanumeric character")
lines=["This is an example","And_this_is_another"]
for line in lines:
	print(line)
	print(re.search(r"\w*", line))
print()

print("Exercise!")
def check_character_groups(text):
	result = re.search(r"\w\s+\w", text)
	return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False