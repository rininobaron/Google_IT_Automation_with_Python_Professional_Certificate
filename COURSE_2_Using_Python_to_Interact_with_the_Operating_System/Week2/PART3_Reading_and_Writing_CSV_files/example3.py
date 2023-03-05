#! /usr/bin/env python3

import os
import time
import csv

print("Visualize file software.csv")
os.system("cat software.csv")
time.sleep(5)
#os.system("cls") # Windows
os.system("clear") # Linux and Unix

with open("software.csv", "r") as software:
	reader = csv.DictReader(software)
	for row in reader:
		time.sleep(1)
		print("{} has {} users".format(row["name"], row["users"]))