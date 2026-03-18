import re

s = input()
pattern = input()
replacement = input()

escaped_pattern = re.escape(pattern)
result = re.sub(escaped_pattern, replacement, s)
print(result)