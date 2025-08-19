# Day 56: Union of Two Number Sets

# Take two sets of numbers from user
set1 = set(map(int, input("Enter numbers for first set (comma-separated): ").split(",")))
set2 = set(map(int, input("Enter numbers for second set (comma-separated): ").split(",")))

# Union
union_set = set1 | set2   # same as set1.union(set2)

print("\nFirst Set:", set1)
print("Second Set:", set2)
print("Union of Sets:", union_set)
