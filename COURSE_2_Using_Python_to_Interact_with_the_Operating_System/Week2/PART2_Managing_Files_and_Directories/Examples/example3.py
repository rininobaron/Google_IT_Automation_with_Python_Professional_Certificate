#! /usr/bin/env python3
import os
import time
import datetime

path="/home/ricardo/Google_IT_Automation_with_Python_Professional_Certificate/COURSE_2_Using_Python_to_Interact_with_the_Operating_System/Week2/PART1_Reading_and_Writing_Files/Examples/"
print("Get file size in bytes")
print(os.path.getsize(path+"spider.txt"))
time.sleep(2)
print()

print("Get the last time the file was modified")
print()
print("Unix timestamp")
print(os.path.getmtime(path+"spider.txt"))
time.sleep(2)
print()
print("datetime")
timestamp = os.path.getmtime(path+"spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))
time.sleep(2)
print()

print("Get full path from this script file")
print(os.path.abspath("example3.py"))
time.sleep(2)
print()
