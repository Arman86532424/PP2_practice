def fact(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i = i + 1
    return f

print("enter number:")
num = int(input())

print(fact(num))
