
while True:
    try:
        initial = input("Enter your account balance: ")
        balance = float(initial)
        if balance < 0:
            print("Balance cannot be negative. Please enter a valid amount.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    print(f"\nCurrent Balance: {balance}")
    amount = input("Enter withdrawal amount (or 'exit' to quit): ")
    if amount.lower() == 'exit':
        print("Thank you for using the ATM!")
        break
    try:
        amount = float(amount)
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        else:
            if amount > balance:
                print("Error: Insufficient funds.")
            else:
                balance -= amount
                print(f"Withdrawal successful! New balance: {balance}")
    except ValueError:
        print("Invalid input. Please enter a number or 'exit'.")