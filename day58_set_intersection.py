# Day 58 - Set Intersection

# Take input from user
set1 = set(map(int, input("Enter numbers for Set 1 (space separated): ").split()))
set2 = set(map(int, input("Enter numbers for Set 2 (space separated): ").split()))

# Intersection
result = set1 & set2   # or set1.intersection(set2)

print("Intersection:", result)
