x =int(input())
if x <= 1:
    print("NO")
else:
    is_prime = True
    for i in range(2,x):
        if x % i == 0:
            is_prime = False
            break

    if is_prime:
        print("YES")
    else:
        print("NO")