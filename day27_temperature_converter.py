# day27_temperature_converter.py

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    print("🌡️ Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose option (1 or 2): ")

    try:
        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            f = celsius_to_fahrenheit(celsius)
            print(f"🌞 {celsius}°C = {f:.2f}°F")
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            c = fahrenheit_to_celsius(fahrenheit)
            print(f"❄️ {fahrenheit}°F = {c:.2f}°C")
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("❌ Please enter a valid number.")
