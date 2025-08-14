# Day 52: Email Slicer

email = input("Enter email: ").strip()

# basic validation
if email.count("@") != 1 or email.startswith("@") or email.endswith("@"):
    print("Invalid email")
else:
    local, domain = email.split("@", 1)
    username = local.split("+", 1)[0]  # handles aliases like name+tag@domain
    print(f"username = {username}")
    print(f"domain = {domain.lower()}")
