# day49_otp_generator.py
import random

print("🔐 OTP Generator")

# Ask user for OTP length
length = input("Enter OTP length (default 6): ")
length = int(length) if length.isdigit() else 6

# Generate OTP
otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])

print(f"✅ Your OTP is: {otp}")
