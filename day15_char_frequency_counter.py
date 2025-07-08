text = input("Enter a string: ")

for char in text:
    count = text.count(char)
    print(f"{char} appears {count} times")
