import re

s = input()
matches = re.findall(r'\d{2,}', s)
if matches:
    print(' '.join(matches))
else:
    print()