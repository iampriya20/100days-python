n = int(input("Enter N: "))
if n < 2:
    print([])
else:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    print(primes)
