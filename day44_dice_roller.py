# day44_dice_roller.py

import random

print("🎲 Dice Roller - User vs Computer")

while True:
    input("\nPress Enter to roll the dice...")

    user_roll = random.randint(1, 6)
    comp_roll = random.randint(1, 6)

    print(f"🧍 You rolled: {user_roll}")
    print(f"💻 Computer rolled: {comp_roll}")

    if user_roll > comp_roll:
        print("🏆 You win!")
    elif user_roll < comp_roll:
        print("😞 Computer wins!")
    else:
        print("🤝 It's a tie!")

    again = input("Roll again? (y/n): ").lower()
    if again != 'y':
        print("👋 Thanks for playing!")
        break
