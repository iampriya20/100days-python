# day36_stopwatch_timer.py

import time

print("⏱️ Stopwatch Timer")
print("Press Enter to start and Enter again to stop.\n")

while True:
    input("➡️ Press Enter to START the timer")
    start_time = time.time()

    input("➡️ Press Enter to STOP the timer")
    end_time = time.time()

    elapsed = end_time - start_time
    print(f"⏳ Elapsed Time: {elapsed:.2f} seconds\n")

    choice = input("Do you want to run the stopwatch again? (y/n): ").lower()
    if choice != 'y':
        print("👋 Goodbye!")
        break
