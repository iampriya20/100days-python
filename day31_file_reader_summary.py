# day31_file_reader_summary.py

file_name = input("Enter filename: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        lines = content.split('\n')
        words = content.split()
        chars = len(content)

        print(f"\n📄 File: {file_name}")
        print(f"🧾 Lines: {len(lines)}")
        print(f"🔤 Words: {len(words)}")
        print(f"🔡 Characters: {chars}")
except FileNotFoundError:
    print("❌ File not found. Make sure the filename is correct.")
