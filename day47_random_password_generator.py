# day47_random_password_generator.py

import random
import string

print("Random Password Generator")

length = int(input("Enter password length: "))
chars = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(chars) for _ in range(length))
print("Your password:", password)
