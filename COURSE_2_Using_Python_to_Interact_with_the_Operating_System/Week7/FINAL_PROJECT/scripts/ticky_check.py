#!/usr/bin/env python3

import csv
import re
import operator

fieldnames_error=["Error", "Count"]
fieldnames_user=["Username", "INFO", "ERROR"]
error_dict = {}
user_dict = {}

path_file="../data/syslog.log"

# Count Errors and INFO per User and Errors by type
with open(path_file, "r") as file:
	lines = file.readlines()
	for line in lines:
		line=line.strip()
		user = re.search(r"\(.*\)$", line)
		user = user[0][1:-1]
		if user not in user_dict.keys():
			user_dict[user]=[0,0]
		error = re.search(r"ERROR [\w' ]*", line)
		info = re.search(r"INFO [\w' ]*", line)
		if error:
			error = error[0].strip()
			error_dict[error[6:]] = error_dict.get(error[6:], 0) + 1
			user_dict[user][1]+=1 
		elif info:
			info = info[0].strip()
			user_dict[user][0]+=1

# Sort dictionaries
error_sorted_list = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)
user_sorted_list = sorted(user_dict.items(), key=operator.itemgetter(0))

# Build the final files

# Build error_message.csv
with open("../data/error_message.csv", "w") as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames_error)
	writer.writeheader()
	for item in error_sorted_list:
		writer.writerow({"Error": item[0], "Count": item[1]})

# Build error_message.csv
with open("../data/user_statistics.csv", "w") as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames_user)
	writer.writeheader()
	for item in user_sorted_list:
		writer.writerow({"Username": item[0], "INFO": item[1][0], "ERROR": item[1][1]})