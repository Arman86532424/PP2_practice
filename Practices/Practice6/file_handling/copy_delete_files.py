import os
import shutil

shutil.copy('raw.txt','dublicate.txt')


file_name = 'dublicate.txt'

if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted.")
else:
    print("File does not exist.")


