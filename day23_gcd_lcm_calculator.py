# day23_gcd_lcm_calculator.py

import math

def calculate_gcd(a, b):
    return math.gcd(a, b)

def calculate_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        gcd = calculate_gcd(num1, num2)
        lcm = calculate_lcm(num1, num2)

        print(f"\n✅ GCD of {num1} and {num2} is: {gcd}")
        print(f"✅ LCM of {num1} and {num2} is: {lcm}")

    except ValueError:
        print("❌ Please enter valid integers.")
