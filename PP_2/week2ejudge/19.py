x = int(input())
ass = {}
for i in range(x):
    a = input().split()
    if a[0] in ass:
        ass[a[0]] += int(a[1])
    else:
        ass[a[0]] = int(a[1])

for key,value in sorted(ass.items()):
    print(key,value)