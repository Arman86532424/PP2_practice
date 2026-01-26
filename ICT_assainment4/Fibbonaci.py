print("Enter a number of trems for fubonacci ")
c = int(input())

if c <= 0:
    print("Please Enter a positive number")
else:
    a,b = 0,1
    print("Fibonacci sequence: ")
    for i in range(c):
        print(a)
        a, b = b , b + a