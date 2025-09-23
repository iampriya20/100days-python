# Day 91: Prime Factorization

def prime_factorization(n: int) -> list:
    """Return the prime factors of a given number n."""
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if num > 1:
        print(f"Prime factors of {num} are: {prime_factorization(num)}")
    else:
        print("Enter a number greater than 1.")
