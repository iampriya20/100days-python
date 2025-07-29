# day35_simple_interest_calculator.py

print("💰 Simple Interest Calculator")

# Get input from the user
p = float(input("Enter Principal amount (₹): "))
r = float(input("Enter Rate of interest (%): "))
t = float(input("Enter Time (in years): "))

# Calculate Simple Interest
si = (p * r * t) / 100

# Print the result
print(f"\n📈 Simple Interest = ₹{si:.2f}")
