# day28_list_statistics.py

def calculate_stats(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)
    return maximum, minimum, average

if __name__ == "__main__":
    try:
        input_str = input("Enter numbers separated by spaces: ")
        number_list = list(map(float, input_str.strip().split()))

        if len(number_list) == 0:
            print("❌ No numbers entered.")
        else:
            max_val, min_val, avg = calculate_stats(number_list)
            print(f"🔺 Maximum: {max_val}")
            print(f"🔻 Minimum: {min_val}")
            print(f"📊 Average: {avg:.2f}")
    except ValueError:
        print("❌ Please enter valid numbers only.")
