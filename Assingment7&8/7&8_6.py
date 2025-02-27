class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
def main():
    account_number = input("Enter the account number: ")
    initial_balance = float(input("Enter the initial balance: "))
    account = BankAccount(account_number, initial_balance)
    account.display()
    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, display, exit): ").lower()
        if action == "deposit":
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif action == "withdraw":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif action == "display":
            account.display()
        elif action == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid action. Please try again.")
main()
