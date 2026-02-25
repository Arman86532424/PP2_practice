def Powers_of_two(x):
    for i in range(x+1):
        yield 2**i

a = int(input())
for i in Powers_of_two(a):
    print(i,end=' ')
