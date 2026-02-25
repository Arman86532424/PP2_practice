def even_nums(n):
    m = 0
    while m <= n:
        yield m
        m += 2

n = int(input())

first = True
for num in even_nums(n):
    if not first:
        print(",", end="")
    print(num, end="")
    first = False