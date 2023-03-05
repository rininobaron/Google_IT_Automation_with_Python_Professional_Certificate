#! /usr/bin/env python3

import csv
import os
import time

print("Visualize file csv_file.txt")
os.system("cat csv_file.txt")
time.sleep(5)
# os.system("cls") # Windows
os.system("clear") # Linux and UNix

file = open("csv_file.txt")
csv_file = csv.reader(file)

for row in csv_file:
	time.sleep(1)
	name, phone, role = row
	print("Name: {}, Phone: {}, Role: {} ".format(name, phone, role))
file.close()