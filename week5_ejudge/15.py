import re

s = input()
result = re.sub(r'\d', lambda m: m.group(0) * 2, s)
print(result)