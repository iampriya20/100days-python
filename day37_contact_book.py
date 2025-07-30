# day37_contact_book.py

print("📖 Contact Book")

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View All Contacts")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"✅ Contact '{name}' added successfully.")

    elif choice == '2':
        if contacts:
            print("\n📋 Contact List:")
            for name, phone in contacts.items():
                print(f"{name} - Phone: {phone}")
        else:
            print("📭 No contacts found.")

    elif choice == '3':
        print("👋 Exiting Contact Book!")
        break

    else:
        print("❌ Invalid option. Try again!")
