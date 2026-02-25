def thing(a,b):
    for i in range(a,(b+1)):
        yield i*i

a = list(map(int,input().split()))

for num in thing(a[0],a[1]):
    print(num)

