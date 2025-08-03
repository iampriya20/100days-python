# day41_file_size_checker.py

from os.path import getsize, isfile

p = input("File path: ")
if isfile(p):
    s = getsize(p)
    print(f"Size: {s} bytes ({s/1024:.2f} KB / {s/1024/1024:.2f} MB)")
else:
    print("❌ File not found!")
