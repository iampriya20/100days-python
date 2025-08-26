# Day 64: Find Second Smallest Number in a List

def second_smallest(numbers: list) -> int:
    unique_nums = list(set(numbers))  # remove duplicates
    if len(unique_nums) < 2:
        return None  # not enough unique numbers
    unique_nums.sort()
    return unique_nums[1]

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers (space separated): ").split()))
    result = second_smallest(nums)
    if result is None:
        print("Not enough unique numbers to find second smallest.")
    else:
        print("Second smallest number:", result)
