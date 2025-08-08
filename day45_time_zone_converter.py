# day45_time_zone_converter.py

from datetime import datetime, date
import pytz

# Common time zones
TIMEZONES = {
    "CST": "US/Central",
    "EST": "US/Eastern",
    "MST": "US/Mountain",
    "PST": "US/Pacific",
    "IST": "Asia/Kolkata",
    "GMT": "Etc/Greenwich",
    "UTC": "UTC",
    "BST": "Europe/London",
    "CET": "Europe/Paris",
    "AEST": "Australia/Sydney"
}

print("🌍 Time Zone Converter")
print("Available:", ", ".join(TIMEZONES.keys()))

src = input("FROM TZ (e.g., CST): ").upper()
dst = input("TO TZ (e.g., IST): ").upper()

if src not in TIMEZONES or dst not in TIMEZONES:
    print("❌ Invalid timezone. Choose from:", ", ".join(TIMEZONES.keys()))
else:
    # Ask for custom date & time
    date_str = input("Enter date (YYYY-MM-DD) [leave blank for today]: ").strip()
    time_str = input("Enter time (HH:MM, 24-hour): ").strip()

    try:
        # Default date to today if blank
        the_date = date.fromisoformat(date_str) if date_str else date.today()

        # Parse time
        hour, minute = map(int, time_str.split(":"))

        # Build naive datetime
        naive_dt = datetime(the_date.year, the_date.month, the_date.day, hour, minute)

        # Localize to source tz, then convert
        src_tz = pytz.timezone(TIMEZONES[src])
        dst_tz = pytz.timezone(TIMEZONES[dst])

        src_dt = src_tz.localize(naive_dt, is_dst=None)  # handle DST correctly
        dst_dt = src_dt.astimezone(dst_tz)

        print(f"\n🕒 {src} {src_dt.strftime('%Y-%m-%d %H:%M')}")
        print(f"-> {dst} {dst_dt.strftime('%Y-%m-%d %H:%M')}")

    except Exception as e:
        print("❌ Invalid input. Use YYYY-MM-DD and HH:MM. Error:", e)
