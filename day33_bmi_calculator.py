# day33_bmi_calculator.py

weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

height_m = height_cm / 100  # convert cm to meters
bmi = weight / (height_m ** 2)

print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are Underweight.")
elif bmi < 25:
    print("You have Normal weight.")
elif bmi < 30:
    print("You are Overweight.")
else:
    print("You are Obese.")
