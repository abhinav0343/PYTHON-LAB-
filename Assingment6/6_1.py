class Password_manager:
    def __init__(self, new_pass):
        self.old_passwords = [new_pass]  # Initialize password history

    def set_password(self, new_passw):
        if new_passw not in self.old_passwords:
            self.old_passwords.append(new_passw)
            print(" Password updated successfully!")
        else:
            print(" Password already exists.")
    def get_password(self):
        return self.old_passwords[-1]
    def is_correct(self, entered_password):
        return entered_password == self.get_password()
    
pm = Password_manager("Chinnu@2007")

while True:
    print("\nMENU : ")
    print("1. Set new password")
    print("2. Get current password")
    print("3. Enter password to verify")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            new_password = input("Enter new password: ")
            pm.set_password(new_password)  # Set new password

        case 2:
            print(f"Current password: {pm.get_password()}")

        case 3:
            entered_password = input("Enter password to verify: ")
            if pm.is_correct(entered_password):
                print(" Password is correct!")
            else:
                print(" Password is incorrect!")

        case 0:
            print(" Exiting program.")
            break 

        case _:
            print("Invalid choice. Please enter a valid option.")
