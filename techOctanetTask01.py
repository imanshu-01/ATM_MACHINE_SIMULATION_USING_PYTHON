class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.pin = "1234"  # Default ATM PIN for simplicity

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Your new balance is ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. Your new balance is ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def authenticate(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin != self.pin:
            print("Incorrect PIN. Access denied.")
            return False
        return True


def atm_machine():
    print("Welcome to the ATM Machine.")
    atm = ATM(1000)  # Set initial balance as $1000

    if atm.authenticate():
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                atm.check_balance()
            elif choice == "2":
                amount = float(input("Enter amount to deposit: $"))
                atm.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: $"))
                atm.withdraw(amount)
            elif choice == "4":
                print("Exiting ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Exiting due to incorrect PIN.")
atm_machine()
