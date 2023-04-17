#! /usr/bin/env python3

import re

print("Look for 'python' or 'Python' word")
print("Python")
print(re.search(r"[Pp]ython", "Python"))
print()

print("Look for word pattern 'way' beginning with any lowercase letter")
lines=["The end of the highway","What a way to go"]
for line in lines:
	print(line)
	print(re.search(r"[a-z]way", line))
print()

print("Look for word pattern 'cloud' ending with any lowercase or upper letter \nor 0 to 9 digits")
words=["cloudy","cloud9","cloudA"]
for word in words:
	print(word)
	print(re.search(r"cloud[a-zA-Z0-9]", word))
print()

print("Exercise!")
def check_punctuation (text):
	result = re.search(r"[,....:;?!]", text)
	return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False
print()

print("Search for any character that's not a letter (Use circunflex)")
print("This is a sentence with spaces.")
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print()

print("Search for any character that's not a letter (Use circunflex)\nbut ignoring spaces")
print("This is a sentence with spaces.")
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
print()

print("Search for an expresion that match waord 'cat' or 'dog'")
lines=["I like cats.","I like dogs.", "I like both dogs and cats."]
for line in lines:
	print(line)
	print(re.search(r"cat|dog", line))
print()

print("Search for all possible matches for words 'cat' and 'dog'")
print("I like both dogs and cats.")
print(re.findall(r"cat|dog", "I like both dogs and cats."))
print()