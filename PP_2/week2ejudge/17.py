a = int(input())
numbers = dict()

for i in range(a):
    x = input()
    if x in numbers:
        numbers[x]+=1
    else:
        numbers[x]=1

counter = 0
for i in numbers.values():
    if i == 3:
        counter += 1

print(counter)
