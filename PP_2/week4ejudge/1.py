def my_generator(n):
    num = 1
    while num < n:
        yield num * num  
        num += 1

x = int(input())
squares = my_generator(x+1)
for square in squares:
    print(square)
