def count_down(n):
    i = n
    for j in range(n+1):
        yield i
        i-=1

a = int(input())
for i in count_down(a):
    print(i)