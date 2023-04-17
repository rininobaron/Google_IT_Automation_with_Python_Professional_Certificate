#! /usr/bin/env python3

import re

print("Look for 'Py' follow by any quantity of any characters and ending \nwith 'n'")
lines=["Pygmalion","Python Ptogramming"]
for line in lines:
	print(line)
	print(re.search(r"Py.*n", line))
print()

print("Look for 'Py' follow by any quantity of any characters and ending \nwith 'n' (only match letters)")
lines=["Python Ptogramming","Pyn"]
for line in lines:
	print(line)
	print(re.search(r"Py[a-z]*n", line))
print()

print("Match all 'o' and 'l' without characters between them")
words=["goldfish","woolly","boil"]
for word in words:
	print(word)
	print(re.search(r"o+l+", word))
print()

print("Exercise!")
def repeating_letter_a(text):
	result = re.search(r"[A|a].*[A|a]", text)
	return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
print()

print("Using character '?'")
words=["To each their own","I like peaches"]
for i in words:
	print(i)
	print(re.search(r"p?each", i))