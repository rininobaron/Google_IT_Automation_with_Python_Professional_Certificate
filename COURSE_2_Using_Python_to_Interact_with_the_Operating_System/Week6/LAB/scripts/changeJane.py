#!/usr/bin/env python3

import sys
import subprocess

old_user="jane"
new_user="jdoe"
with open(sys.argv[1], "r") as files:
	files=files.readlines()
	for file in files:
		file=file.strip()
		new_file=file.replace(old_user, new_user)
		subprocess.run(["mv", file, new_file])
