import re

s = input()
word_pattern = re.compile(r'\b\w+\b')
words = word_pattern.findall(s)
print(len(words))