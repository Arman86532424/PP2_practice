thislist = ["apple", 'banana','cherrry',"orange","kiwi","mango"]

i =0
while i < len(thislist):
    print(thislist[i])
    i+=1

new_list = [x for x in thislist if "a" in x] #list comprehension
print(new_list)

