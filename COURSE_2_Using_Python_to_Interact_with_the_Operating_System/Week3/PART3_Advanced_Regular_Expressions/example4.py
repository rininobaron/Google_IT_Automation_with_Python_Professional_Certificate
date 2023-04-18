#! /usr/bin/env python3

import re

print("Use split function")
line="One sentence. Another one? And the last one!"
regex=r"[.?!]"
print(line)
print(re.split(regex, line))
print()

print("Use split function (including separtors)")
regex=r"([.?!])"
print(line)
print(re.split(regex, line))
print()

print("Use sub (substituing)")
line="Received an email for go_nuts95@my.example-com"
regex=r"[\w.%+-]+@[\w.-]+"
print(line)
print(re.sub(regex, "[REDACTED]", line))
print()

print("Use sub for swaping groups using second regex statement")
line="Lovelace, Ada"
regex=r"^([\w.-]*), ([\w.-]*)$"
regex2=r"\2 \1"
print(line)
print(re.sub(regex, regex2, line))
print()