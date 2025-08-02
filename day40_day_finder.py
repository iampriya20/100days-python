# day40_day_finder.py

import datetime

d = int(input("Day (1-31): "))
m = int(input("Month (1-12): "))
y = int(input("Year: "))

try:
    date = datetime.date(y, m, d)
    print(f"\n🗓️ {date} is a {date.strftime('%A')}")
except:
    print("❌ Invalid date!")
