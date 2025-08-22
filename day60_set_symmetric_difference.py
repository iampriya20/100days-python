# Day 60: Set Symmetric Difference

def parse_input(prompt):
    return set(map(int, input(prompt).replace(",", " ").split()))

set1 = parse_input("Enter numbers for Set 1: ")
set2 = parse_input("Enter numbers for Set 2: ")

# symmetric difference
print("Symmetric Difference:", set1 ^ set2)  
# or set1.symmetric_difference(set2)
