print('Before======================================================================================')
o = open("raw.txt", 'r')
print(o.read())

o = open("raw.txt",'a') 

o.write("I cant use wright mode")

print('After=======================================================================================')
o = open("raw.txt", 'r')
print(o.read())