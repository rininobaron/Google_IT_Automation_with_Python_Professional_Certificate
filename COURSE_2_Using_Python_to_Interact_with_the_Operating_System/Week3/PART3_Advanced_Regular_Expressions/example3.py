#! /usr/bin/env python3

import re

print("Use escape characters")
lines=["Acompletely different string that also has numbers [34567]",\
"99 elephants in a [cage]"]
regex=r"\[(\d+)\]"
for line in lines:
	print(line)
	try:
		print(re.search(regex, line)[1])
	except Exception as e:
		print(e)
print()

print("Use function")
def extract_pid(log_line):
	regex = r"\[(\d+)\]"
	result = re.search(regex, log_line)
	if result is None:
		return ""
	return result[1]
for line in lines:
	print(line)
	print(extract_pid(line))
print()

print("Exercise!")
def extract_pid(log_line):
	regex = r"\[(\d+)\]: ([A-Z]+)"
	result = re.findall(regex, log_line)
	if len(result) == 0:
		return None
	return "{} ({})".format(result[0][0],result[0][1])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
print()