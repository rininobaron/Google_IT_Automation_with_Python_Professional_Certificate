#! /usr/bin/env python3

import os

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
fruit = os.environ.get("FRUIT", "")
print("FRUIT: " + fruit)

if fruit == "":
	os.environ["FRUIT"]="Pineapple" # Same to type this "export FRUIT=Pineapple"
	fruit = os.environ.get("FRUIT", "")
	print("FRUIT: " + fruit)

# Delete envioronment variable
os.system("unset FRUIT")
