def remove_duplicates(items):
    """Removes duplicates while preserving order."""
    return list(dict.fromkeys(items))

if __name__ == "__main__":
    raw = input("Enter items separated by spaces (e.g., 1 2 2 3 4 4 or a b a c): ").strip()

    if not raw:
        print("No input provided.")
    else:
        items = raw.split()
        unique_items = remove_duplicates(items)
        print("Original list:", items)
        print("Without duplicates:", unique_items)