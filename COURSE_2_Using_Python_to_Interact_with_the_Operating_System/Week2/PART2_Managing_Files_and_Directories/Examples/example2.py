#! /usr/bin/env python3
import os
import time

# Add extra funny txt file
os.system("touch hola.txt")

print("Create text file")
os.system("echo 'Hola Mundo' > prueba.txt")
time.sleep(2)
print()

print("Show files in current directory")
os.system("ls")
time.sleep(2)
print()

print("Rename text file")
os.rename("prueba.txt", "finished_masterpiece.txt")
time.sleep(2)
print()

print("Show files in current directory")
os.system("ls")
time.sleep(2)
print()

print("Check if finished_masterpiece.txt file exists using os.path")
print(os.path.exists("finished_masterpiece.txt"))
time.sleep(2)
print()

print("Check if userlist.txt file exists using os.path")
print(os.path.exists("userlist.txt"))
time.sleep(2)
print()

print("Delete text files")
for file in os.listdir():
	if file[-4:] == ".txt":
		os.remove(file)
print("Check files in current directory again")
os.system("ls")
time.sleep(2)
print()