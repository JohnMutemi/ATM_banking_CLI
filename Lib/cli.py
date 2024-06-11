from models import User, Transaction

class BankATM:
    def __init__(self):
        pass

    def login(self):
        username = input("Enter your username: ")
        pin = input("Enter your pin: ")
        user = User.find_by_username(username)
        if user and user.pin == pin:
            return user.id
        else:
            print("Invalid username or pin.")
            return None

    def create_user(self):
        username = input("Enter a new username: ")
        pin = input("Enter a new pin: ")
        user = User(username, pin)
        user.save()
        print(f"User created with ID {user.id}")

    def delete_user(self, user_id):
        user = User.find_by_id(user_id)
        if user:
            user.delete()
            print("User deleted successfully.")
        else:
            print("User not found.")

    def deposit(self, user_id):
        user = User.find_by_id(user_id)
        if user:
            amount = float(input("Enter amount to deposit: "))
            user.update_balance(amount)
            transaction = Transaction(user_id, amount, "deposit")
            transaction.save()
            print(f"Deposited {amount}. New balance is {user.balance}.")
        else:
            print("User not found.")

    def withdraw(self, user_id):
        user = User.find_by_id(user_id)
        if user:
            amount = float(input("Enter amount to withdraw: "))
            if user.balance >= amount:
                user.update_balance(-amount)
                transaction = Transaction(user_id, amount, "withdraw")
                transaction.save()
                print(f"Withdrew {amount}. New balance is {user.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("User not found.")

    def view_balance(self, user_id):
        user = User.find_by_id(user_id)
        if user:
            print(f"Current balance: {user.balance}")
        else:
            print("User not found.")

    def pay_bill(self, user_id):
        user = User.find_by_id(user_id)
        if user:
            bill_type = input("Enter bill type (electric, water, gas): ").lower()
            amount = float(input(f"Enter amount to pay for {bill_type} bill: "))
            if user.balance >= amount:
                user.update_balance(-amount)
                transaction = Transaction(user_id, amount, f"pay_{bill_type}_bill")
                transaction.save()
                print(f"Paid {amount} for {bill_type} bill. New balance is {user.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("User not found.")

def main():
    atm = BankATM()
    while True:
        print("\n--- Bank ATM ---")
        print("1. Create User")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            atm.create_user()
        elif choice == "2":
            user_id = atm.login()
            if user_id:
                while True:
                    print("\n--- User Menu ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. View Balance")
                    print("4. Pay Bill")
                    print("5. Delete Account")
                    print("6. Logout")
                    user_choice = input("Choose an option: ")
                    if user_choice == "1":
                        atm.deposit(user_id)
                    elif user_choice == "2":
                        atm.withdraw(user_id)
                    elif user_choice == "3":
                        atm.view_balance(user_id)
                    elif user_choice == "4":
                        atm.pay_bill(user_id)
                    elif user_choice == "5":
                        atm.delete_user(user_id)
                        break
                    elif user_choice == "6":
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()