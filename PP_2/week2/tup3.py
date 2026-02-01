#way tp change a tuple
x = ("apple", "orange","banana")
y = list(x)
y[1] = 'kiwi'
x = tuple(y)

#combination of tuples
c = ('green',)
x += c
print(x)