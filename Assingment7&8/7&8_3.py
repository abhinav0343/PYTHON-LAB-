class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {} 

    def create_account(self):
        account_number = int(input("Enter a account number: "))
        if account_number in self.accounts:
            print("Account already exists! Try again.")
            return

        customer_name = input("Enter your name: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        self.accounts[account_number] = {"name": customer_name, "balance": initial_deposit}
        print(f"\n Account created successfully")

    def deposit(self):
        account_number = int(input("\nEnter your account number: "))
        if account_number not in self.accounts:
            print("Account not found!")
            return
        amount = float(input("Enter amount to deposit: "))
        self.accounts[account_number]["balance"] += amount
        print(f"{amount} deposited successfully! New Balance: {self.accounts[account_number]['balance']}")

    def withdraw(self):
        account_number = int(input("Enter your account number: "))
        if account_number not in self.accounts:
            print("Account not found!")
            return
        amount = float(input("Enter amount to withdraw: "))
        if self.accounts[account_number]["balance"] < amount:
            print("\nInsufficient funds!")
            return
        self.accounts[account_number]["balance"] -= amount
        print(f"withdrawn successfully! New Balance: {self.accounts[account_number]['balance']}")

    def check_balance(self):
        account_number = int(input("\nEnter your account number: "))
        if account_number not in self.accounts:
            print("Account not found!")
            return
        print(f"Account Balance for {self.accounts[account_number]['name']}: {self.accounts[account_number]['balance']}")

bank = Bank("ABHI Bank")
while True:
    print("\nenter the choice as mentioned below \n")
    print("1️.Create Account")
    print("2️.Deposit Money")
    print("3️.Withdraw Money")
    print("4️.Check Balance")
    print("0️.Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.deposit()
    elif choice == "3":
        bank.withdraw()
    elif choice == "4":
        bank.check_balance()
    elif choice == "0":
        print("\n ***EXITING*** \n")
        break
    else:
        print("\nInvalid choice! Please select a valid option.")
