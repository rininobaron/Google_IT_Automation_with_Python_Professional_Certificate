#! /usr/bin/env python3
import os
import time

print("Create text file")
os.system("echo 'Hola Mundo' > prueba.txt")
time.sleep(2)
print()

print("Show files in current directory")
os.system("ls -l")
time.sleep(2)
print()

print("Show text file content")
os.system("cat prueba.txt")
time.sleep(2)
print()

print("Remove text file")
os.remove("prueba.txt")
time.sleep(2)
print()

print("Show files in current directory")
os.system("ls -l")
time.sleep(2)
print()
