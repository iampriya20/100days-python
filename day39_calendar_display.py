# day39_calendar_display.py

import calendar

print("📅 Calendar Display")

# Input: month and year
year = int(input("Enter year : "))
month = int(input("Enter month (1-12): "))

# Display calendar
print("\n" + calendar.month(year, month))
