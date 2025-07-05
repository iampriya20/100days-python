# Day 13: Prime Numbers in a Given Range

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:  # 1 is not prime
        for i in range(2, int(num ** 0.5) + 1):  # Optimization: check up to square root
            if num % i == 0:
                break
        else:
            print(num)
