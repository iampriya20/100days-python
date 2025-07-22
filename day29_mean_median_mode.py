# day30_mean_median_mode.py

import statistics

def calculate_stats(numbers):
    mean_val = statistics.mean(numbers)
    median_val = statistics.median(numbers)
    try:
        mode_val = statistics.mode(numbers)
    except statistics.StatisticsError:
        mode_val = "No unique mode"
    return mean_val, median_val, mode_val

if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        number_list = list(map(float, user_input.strip().split()))

        if len(number_list) == 0:
            print("❌ No numbers entered.")
        else:
            mean, median, mode = calculate_stats(number_list)
            print(f"📊 Mean: {mean:.2f}")
            print(f"📉 Median: {median}")
            print(f"🔁 Mode: {mode}")
    except ValueError:
        print("❌ Please enter valid numbers only.")
