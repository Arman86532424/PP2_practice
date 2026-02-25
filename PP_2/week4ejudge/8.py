def primes_up_to(x):
    for num in range(2, x + 1):
        is_prime = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            yield num



n = int(input())
for p in primes_up_to(n):
    print(p, end=" ")