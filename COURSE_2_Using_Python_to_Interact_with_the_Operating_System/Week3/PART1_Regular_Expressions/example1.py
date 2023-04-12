#! /usr/bin/env python3

import re

# Using index method
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index+1:index+6])

#Using Regex syntax
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])