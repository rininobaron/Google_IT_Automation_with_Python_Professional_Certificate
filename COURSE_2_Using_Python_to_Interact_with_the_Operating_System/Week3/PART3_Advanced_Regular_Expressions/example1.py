#! /usr/bin/env python3

import re

print("Example 1")
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print("Use groups method")
print(result[0])
print(result.groups())
for i in range(len(result.groups())+1):
	print(result[i])
print("{}{}".format(result[2], result[1]))
print()

print("Using a function")

def rearrange_name(name):
	result = re.search(r"^(\w*), (\w* ?[A-Z]?[.]?)$", name)
	#result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
	if result==None:
		return name
	return print("{} {}".format(result[2], result[1]))

names=["Lovelace, Ada","Ritchie, Dennis", "Hopper, Grace M.", "Kennedy, John F."]
for name in names:
	rearrange_name(name)