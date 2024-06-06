# Base class for all accounts
class Account:
    def __init__(self, account_number, account_holder):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited {amount} to account {self._account_number}. New balance: {self._balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return f"Withdrew {amount} from account {self._account_number}. New balance: {self._balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account Number: {self._account_number}, Account Holder: {self._account_holder}, Balance: {self._balance}"


# SavingsAccount with interest and withdrawal limit
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.interest_rate = 0.005
        self.withdrawal_limit = 700000

    def deposit(self, amount):
        message = super().deposit(amount)
        interest = amount * self.interest_rate
        self._balance += interest
        return f"{message}\nInterest of {interest} added. New balance: {self._balance}"

    def withdraw(self, amount):
        if amount <= self.withdrawal_limit:
            return super().withdraw(amount)
        else:
            return "Withdrawal amount exceeds the limit for Savings Account."


# CurrentAccount with no restrictions
class CurrentAccount(Account):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)


# ChildrensAccount with interest and no withdrawals
class ChildrensAccount(Account):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.interest_rate = 0.007

    def deposit(self, amount):
        message = super().deposit(amount)
        interest = amount * self.interest_rate
        self._balance += interest
        return f"{message}\nInterest of {interest} added. New balance: {self._balance}"

    def withdraw(self, amount):
        return "Withdrawals are not allowed from Children's Account."


# StudentAccount with deposit and withdrawal limits
class StudentAccount(Account):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.withdrawal_limit = 2000
        self.deposit_limit = 50000

    def deposit(self, amount):
        if amount <= self.deposit_limit:
            return super().deposit(amount)
        else:
            return "Deposit amount exceeds the limit for Student Account."

    def withdraw(self, amount):
        if amount <= self.withdrawal_limit:
            return super().withdraw(amount)
        else:
            return "Withdrawal amount exceeds the limit for Student Account."


def main():
    accounts = {}

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAccount Types:")
            print("1. Savings")
            print("2. Current")
            print("3. Children's")
            print("4. Student")

            account_type = input("Select account type: ")
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder's name: ")

            if account_number in accounts:
                print("Account number already exists.")
                continue

            if account_type == '1':
                accounts[account_number] = SavingsAccount(account_number, account_holder)
            elif account_type == '2':
                accounts[account_number] = CurrentAccount(account_number, account_holder)
            elif account_type == '3':
                accounts[account_number] = ChildrensAccount(account_number, account_holder)
            elif account_type == '4':
                accounts[account_number] = StudentAccount(account_number, account_holder)
            else:
                print("Invalid account type.")

        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))

            if account_number in accounts:
                message = accounts[account_number].deposit(amount)
                print(message)
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))

            if account_number in accounts:
                message = accounts[account_number].withdraw(amount)
                print(message)
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = input("Enter account number: ")

            if account_number in accounts:
                print(accounts[account_number])
            else:
                print("Account not found.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
