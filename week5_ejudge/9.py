import re

s = input()
matches = re.findall(r'\b[A-Za-z]{3}\b', s)
print(len(matches))