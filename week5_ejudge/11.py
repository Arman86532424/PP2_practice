import re

s = input()
uppercase_count = len(re.findall(r'[A-Z]', s))
print(uppercase_count)