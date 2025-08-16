# Day 53: Password Masker
from getpass import getpass

pw = getpass("Enter password: ")
mask_char = "*"
print(f"Masked: {mask_char * len(pw)} ({len(pw)} chars)")
