
class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Error: Insufficient funds. Your balance is {self.balance}.")
            return False
        elif amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: {self.balance}")
            return True


    def show_balance(self):
        print(f"Current balance: {self.balance}")

if __name__ == "__main__":
    atm = ATM(balance=10000)
    while True:
        print("\nATM Menu:")
        print("1. Show Balance")
        print("2. Withdraw")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            atm.show_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please try again.")

