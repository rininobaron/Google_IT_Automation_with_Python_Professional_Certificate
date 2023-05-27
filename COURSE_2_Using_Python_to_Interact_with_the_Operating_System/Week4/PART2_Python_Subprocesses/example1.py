#! /usr/bin/env python3

import subprocess

print(subprocess.run(["date"]))
print()

print(subprocess.run(["sleep", "2"]))
print()

print(subprocess.run(["ls", "this_file_does_not_exist"]))
print()
