# Day 64: Find Second Largest Number in a List

def second_largest(numbers: list) -> int:
    unique_nums = list(set(numbers))  # remove duplicates
    if len(unique_nums) < 2:
        return None  # no second largest
    unique_nums.sort(reverse=True)
    return unique_nums[1]

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers (space separated): ").split()))
    result = second_largest(nums)
    if result is None:
        print("Not enough unique numbers to find second largest.")
    else:
        print("Second largest number:", result)
