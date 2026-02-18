a = int(input())
strs = {}
for i in range(a):
    x = input()
    if x in strs:
        continue
    else:
        strs[x] = i+1

for keys,values in sorted(strs.items()):
    print(keys,values)

