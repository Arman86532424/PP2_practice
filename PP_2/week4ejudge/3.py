def divisible(n):
    i = 0
    p = 0
    while p <= n:
        yield p
        i+=1
        p = i * 12

x = int(input())
for num in divisible(x):
    print(num,end=' ')


