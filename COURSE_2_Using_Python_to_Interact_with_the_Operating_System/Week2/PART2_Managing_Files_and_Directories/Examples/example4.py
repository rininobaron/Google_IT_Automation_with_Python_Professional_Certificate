#! /usr/bin/env python3
import os
import time

print()

new_dir = "new_dir"

print("Get current directory")
print(os.getcwd())
time.sleep(2)
print()

print("Create a directory")
os.mkdir(new_dir)
time.sleep(2)
print()

print("Show content in current directory")
print(" ".join(os.listdir()))
time.sleep(2)
print()

print("Print current directory")
print(os.path.abspath(""))
time.sleep(2)
print()

print("Change to new directory")
os.chdir(new_dir)
time.sleep(2)
print()

print("Print new current directory")
print(os.getcwd())
time.sleep(2)
print()

print("Return to previous directory")
os.chdir("..")
time.sleep(2)
print()

print("Delete "+new_dir+" directory")
os.rmdir(new_dir)
time.sleep(2)
print()

print("Show content in current directory")
print(" ".join(os.listdir()))
time.sleep(2)
print()

print("Create files and diretories like the video")
dir_="website"
os.mkdir(dir_)
os.mkdir(dir_+"/images")
with open(dir_+"/index.html","w") as file:
	file.write("")
with open(dir_+"/favicon.ico","w") as file:
	file.write("")
print("Success!")
time.sleep(2)
print()

print("Show if the item is file or directory in "+dir_)
for item in os.listdir(dir_):
	fullname = os.path.join(dir_,item)
	if os.path.isdir(fullname):
		print("{} is a directory".format(fullname))
	else:
		print("{} is a file".format(fullname))
time.sleep(2)
print()

print("Delete example files and directories created in this script")
for item in os.listdir():
	if item[-3:]==".py":
		continue
	if os.path.isdir(item):
		os.system("rm -rf "+item)
	else:
		os.remove(item)