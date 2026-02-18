x = int(input())
i = 1
while i <= x:
    if i == x:
        print("YES")
        break
    i *= 2

if i != x:
    print("NO")