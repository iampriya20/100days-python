def caesar(text, shift):
    shift %= 26
    out = []
    for ch in text:
        if 'a' <= ch <= 'z':
            out.append(chr((ord(ch) - 97 + shift) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            out.append(chr((ord(ch) - 65 + shift) % 26 + 65))
        else:
            out.append(ch)
    return ''.join(out)

mode = input("Encrypt or Decrypt? (e/d): ").strip().lower()
text = input("Enter text: ")
shift = int(input("Enter shift (e.g., 3 or -3): "))

if mode == 'e':
    print("Encrypted:", caesar(text, shift))
elif mode == 'd':
    print("Decrypted:", caesar(text, -shift))
else:
    print("Invalid mode. Use 'e' or 'd'.")
