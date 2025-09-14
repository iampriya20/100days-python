"""
Day 83: Mini ATM Simulation

Features:
- Deposit, Withdraw (with sufficient-balance check), Check Balance
- Mini statement (recent transactions)
- Simple input validation + looped menu
"""

from datetime import datetime

def fmt(amount):
    return f"${amount:,.2f}"

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def print_menu():
    print("\n=== MINI ATM ===")
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Balance")
    print("4) Mini Statement (last 10)")
    print("5) Exit")

def mini_statement(txns, limit=10):
    print("\n--- Mini Statement ---")
    if not txns:
        print("No transactions yet.")
        return
    for t in txns[-limit:]:
        print(f"[{t['time']}] {t['type']}: {fmt(t['amount'])} -> Balance: {fmt(t['balance'])}")

def main():
    # Optional: start with a custom opening balance
    opening = input("Enter opening balance (blank for 0): ").strip()
    balance = 0.0
    if opening:
        try:
            balance = float(opening)
            if balance < 0:
                print("Opening balance cannot be negative. Using 0.")
                balance = 0.0
        except ValueError:
            print("Invalid number. Using 0.")

    transactions = []
    if balance > 0:
        transactions.append({"time": now(), "type": "OPEN", "amount": balance, "balance": balance})

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":  # Deposit
            amt_str = input("Enter deposit amount: ").strip()
            try:
                amt = float(amt_str)
                if amt <= 0:
                    print("Amount must be positive.")
                    continue
                balance += amt
                transactions.append({"time": now(), "type": "DEPOSIT", "amount": amt, "balance": balance})
                print(f"Deposited {fmt(amt)}. New balance: {fmt(balance)}")
            except ValueError:
                print("Invalid amount.")

        elif choice == "2":  # Withdraw
            amt_str = input("Enter withdrawal amount: ").strip()
            try:
                amt = float(amt_str)
                if amt <= 0:
                    print("Amount must be positive.")
                    continue
                if amt > balance:
                    print(f"Insufficient funds. Available: {fmt(balance)}")
                    continue
                balance -= amt
                transactions.append({"time": now(), "type": "WITHDRAW", "amount": amt, "balance": balance})
                print(f"Withdrew {fmt(amt)}. New balance: {fmt(balance)}")
            except ValueError:
                print("Invalid amount.")

        elif choice == "3":  # Balance
            print(f"\nCurrent balance: {fmt(balance)}")

        elif choice == "4":  # Mini statement
            mini_statement(transactions, limit=10)

        elif choice == "5":  # Exit
            print("\nThank you for using Mini ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1–5.")

if __name__ == "__main__":
    main()
