x = int(input())
pos = 0
numbers = list(map(int, input().split()))
for i in numbers:
    if i > 0:
        pos +=1

print(pos)