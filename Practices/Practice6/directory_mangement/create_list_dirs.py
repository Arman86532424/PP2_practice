import os

os.makedirs("folder/subfolder/inner")

for i in os.listdir():
    print(i)