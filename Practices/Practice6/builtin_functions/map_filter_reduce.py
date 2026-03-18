import functools

numbers = [1, 2, 3, 4, 5]


squared = list(map(lambda x: x**2, numbers))


evens = list(filter(lambda x: x % 2 == 0, numbers))

print(squared)
print(evens)

#======================================================================================================================
def summm(a,b):   #reduce is simmilar to for, 
    return a+b

prices = [6500, 2400, 50, 30678]
total = functools.reduce(summm,prices) #or i  can use lamda function (lambda x , y :x + y ,prices)

print(total)


