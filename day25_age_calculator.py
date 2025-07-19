# day25_age_calculator.py

from datetime import datetime, timedelta

def calculate_exact_age(birthdate):
    today = datetime.today()

    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        # Borrow days from the previous month
        prev_month = today.replace(day=1) - timedelta(days=1)
        days += prev_month.day

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

if __name__ == "__main__":
    try:
        dob_input = input("Enter your birthdate (YYYY-MM-DD): ")
        birthdate = datetime.strptime(dob_input, "%Y-%m-%d")
        years, months, days = calculate_exact_age(birthdate)

        print(f"🎂 You are {years} years, {months} months, and {days} days old.")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")
