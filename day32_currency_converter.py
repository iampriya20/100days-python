# day32_currency_converter.py

# Set the conversion rate globally
rate = 86.50  # 1 USD = 86.50 INR (latest rate)

def usd_to_inr(usd_amount):
    return usd_amount * rate

if __name__ == "__main__":
    print("💱 Convert USD to INR")

    try:
        usd = float(input("Enter amount in USD: "))
        inr = usd_to_inr(usd)
        print(f"\n💸 {usd} USD = {inr:.2f} INR (Rate: ₹{rate}/USD)")
    except ValueError:
        print("❌ Please enter a valid number.")
