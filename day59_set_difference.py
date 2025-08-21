# day59_set_difference.py

def parse_input(prompt):
    return set(map(int, input(prompt).replace(",", " ").split()))

set1 = parse_input("Enter numbers for Set 1: ")
set2 = parse_input("Enter numbers for Set 2: ")

print("Difference (Set1 - Set2):", set1 - set2)
