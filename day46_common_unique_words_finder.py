print("📝 Common & Unique Words Finder")

# Take two text inputs
text1 = input("Enter first text: ").lower().split()
text2 = input("Enter second text: ").lower().split()

# Convert to sets
set1 = set(text1)
set2 = set(text2)

# Find common and unique words
common_words = set1 & set2
unique_text1 = set1 - set2
unique_text2 = set2 - set1

# Display results
print("\n📌 Common words:", common_words if common_words else "None")
print("📌 Unique to first text:", unique_text1 if unique_text1 else "None")
print("📌 Unique to second text:", unique_text2 if unique_text2 else "None")
