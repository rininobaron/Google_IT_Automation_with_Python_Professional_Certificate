#! /usr/bin/env python3

import os

# Search word with "thon" in a file
print("grep thon /usr/share/dict/words")
os.system("grep thon /usr/share/dict/words")
os.system("sleep 3")
os.system("clear")

# Search a word regardless case (upper or lower)
print("grep -i python /usr/share/dict/words")
os.system("grep -i python /usr/share/dict/words")
os.system("sleep 3")
os.system("clear")

# Search a word with any character using wildcard character '.' (dot)
print("grep l.rts /usr/share/dict/words")
os.system("grep l.rts /usr/share/dict/words")
os.system("sleep 3")
os.system("clear")

# Search all lines begining with a pattern using '^'
print("grep ^fruit /usr/share/dict/words")
os.system("grep ^fruit /usr/share/dict/words")
os.system("sleep 3")
os.system("clear")

# # Search all lines ending with a pattern using '$'
print("grep cat$ /usr/share/dict/words")
os.system("grep cat$ /usr/share/dict/words")
os.system("sleep 3")
os.system("clear")