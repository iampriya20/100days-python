# day42_countdown_timer.py

import time

print("⏳ Countdown Timer")
secs = int(input("Enter seconds: "))

for i in range(secs, 0, -1):
    print(f"{i}...", end="\r")
    time.sleep(1)

print("⏰ Time's up!        ")
