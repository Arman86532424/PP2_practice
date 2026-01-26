def ad(a, b):
    return a + b

def sub(a, b):
    return a - b

def dev(a, b):
    return a / b

def mul(a, b):
    return a * b

n1 = int(input("Enter first number: "))
com = input("Choose operation: ")
n2 = int(input("Enter second number: "))

if com == "add":
    s = ad(n1, n2)
elif com == "subtract":
    s = sub(n1, n2)
elif com == "devide":
    s = dev(n1, n2)
elif com == "multiply":
    s = mul(n1, n2)
else:
    s = "Invalid operation"

print(s)




