#! /usr/bin/env python3

import os
import csv

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open("hosts.cvs", "w") as hosts_csv:
	writer = csv.writer(hosts_csv)
	writer.writerows(hosts)

os.system("cat hosts.cvs")