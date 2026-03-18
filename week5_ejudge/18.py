import re

s = input()
p = input()
escaped = re.escape(p)
count = len(re.findall(escaped, s))
print(count)