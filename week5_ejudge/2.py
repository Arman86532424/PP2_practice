import re

s = input()
sub = input()
if re.search(re.escape(sub), s):
    print("Yes")
else:
    print("No")