n = int(input("Enter a number: "))

if n <= 1:
    print(n, "is not a prime number")
else:
    isp = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            isp = False
            break
    if isp:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")