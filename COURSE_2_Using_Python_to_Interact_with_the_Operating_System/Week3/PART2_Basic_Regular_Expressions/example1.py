#! /usr/bin/env python3

import re

print("Use 'aza'")
for word in ["plaza","bazaar","maze"]:
	print(word)
	result = re.search(r"aza",word)
	print(result)
print()

print("Use circunflex")
print("xenon")
print(re.search(r"^x", "xenon"))
print()

print("Use dot")
for word in ["penguin","clapping","sponge"]:
	print(word)
	print(re.search(r"p.ng", word))
print()

print("Ignore case")
print("Pangaea")
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
print()