import logging
import sys

logging.basicConfig(
    filename='transactions.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ATMMachine:
    def __init__(self, initial_balance=5000.0):
        self.balance = initial_balance

    def check_balance(self) -> None:
        print(f"Balance: {self.balance:.2f} GEL")

    def deposit(self) -> None:
        amount = float(input("Enter deposit amount: "))
        if amount > 1000:
            print("Error: Deposit limit exceeded!")
            return
        if amount <= 0:
            print("Error: Invalid amount")
            return

        self.balance += amount
        msg = f"Deposited: {amount:.2f} GEL | Balance: {self.balance:.2f} GEL"
        print(msg)
        logging.info(msg)

    def withdraw(self) -> None:
        amount = float(input("Enter withdrawal amount: "))
        if amount > self.balance:
            print(f"Error: Insufficient funds")
            return
        if amount <= 0:
            print("Error: Invalid amount")
            return

        self.balance -= amount
        msg = f"Withdrew: {amount:.2f} GEL | Balance: {self.balance:.2f} GEL"
        print(msg)
        logging.info(msg)

    def exit_atm(self) -> None:
        print("Exiting the ATM")
        sys.exit(0)

    def run(self):
        actions = {
            '1': self.check_balance,
            '2': self.withdraw,
            '3': self.deposit,
            '4': self.exit_atm
        }

        print("<--- ATM Machine --->")
        menu = "1. Check balance\n2. Withdraw\n3. Deposit\n4. Exit\nChoose an action: "

        while True:
            print("<----- Menu ----->")
            choice = input(menu)
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid selection.")
            print()

if __name__ == "__main__":
    atm = ATMMachine()
    atm.run()