# Simple Banking System - OOP Concepts Demo

class Account:
    """Class representing a Bank Account with encapsulation"""
    
    def __init__(self, account_number, account_holder, balance=0):
        # Private attributes (encapsulation)
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
    
    # Getters (public methods to access private data)
    def get_account_number(self):
        return self.__account_number
    
    def get_account_holder(self):
        return self.__account_holder
    
    def get_balance(self):
        return self.__balance
    
    # Methods
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✓ Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("❌ Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"❌ Insufficient balance! Available: ${self.__balance}")
        elif amount > 0:
            self.__balance -= amount
            print(f"✓ Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("❌ Withdrawal amount must be positive")
    
    def display_info(self):
        print(f"\n{'='*40}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: ${self.__balance}")
        print(f"{'='*40}")


class SavingsAccount(Account):
    """Savings Account - Inherits from Account (Inheritance)"""
    
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.04):
        super().__init__(account_number, account_holder, balance)
        self.__interest_rate = interest_rate
    
    def add_interest(self):
        """Calculate and add interest to the account"""
        interest = self.get_balance() * self.__interest_rate
        print(f"\n💰 Interest of ${interest:.2f} added ({self.__interest_rate*100}% per annum)")
        self.deposit(interest)
    
    def display_info(self):
        super().display_info()
        print(f"Account Type: Savings")
        print(f"Interest Rate: {self.__interest_rate*100}%")
        print(f"{'='*40}\n")


class CheckingAccount(Account):
    """Checking Account - Inherits from Account (Inheritance)"""
    
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.__overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        """Override withdraw method to allow overdraft (Polymorphism)"""
        available = self.get_balance() + self.__overdraft_limit
        
        if amount > available:
            print(f"❌ Amount exceeds overdraft limit! Available: ${available}")
        elif amount > 0:
            if amount > self.get_balance():
                overdraft_used = amount - self.get_balance()
                print(f"⚠️ Using overdraft: ${overdraft_used:.2f}")
            super().withdraw(amount)
        else:
            print("❌ Withdrawal amount must be positive")
    
    def display_info(self):
        super().display_info()
        print(f"Account Type: Checking")
        print(f"Overdraft Limit: ${self.__overdraft_limit}")
        print(f"{'='*40}\n")


# ============================
# DEMO - Simple Usage
# ============================

print("\n" + "="*50)
print("SIMPLE BANKING SYSTEM - INTERACTIVE")
print("="*50)

# ============================
# INTERACTIVE MENU SYSTEM
# ============================

def display_menu():
    print("\n--- MENU ---")
    print("1. Create Savings Account")
    print("2. Create Checking Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. View Account Info")
    print("6. Add Interest (Savings Account)")
    print("7. Exit")
    print("-" * 40)

accounts = {}  # Dictionary to store accounts

while True:
    display_menu()
    choice = input("Enter your choice (1-7): ").strip()
    
    if choice == "1":
        # Create Savings Account
        acc_num = input("Enter account number: ").strip()
        acc_holder = input("Enter account holder name: ").strip()
        try:
            balance = int(float(input("Enter initial balance: $")))
            interest_rate = float(input("Enter interest rate (e.g., 0.05 for 5%): "))
            accounts[acc_num] = SavingsAccount(acc_num, acc_holder, balance, interest_rate)
            print(f"✓ Savings Account '{acc_num}' created successfully!")
        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.")
    
    elif choice == "2":
        # Create Checking Account
        acc_num = input("Enter account number: ").strip()
        acc_holder = input("Enter account holder name: ").strip()
        try:
            balance = int(float(input("Enter initial balance: $")))
            overdraft = int(float(input("Enter overdraft limit: $")))
            accounts[acc_num] = CheckingAccount(acc_num, acc_holder, balance, overdraft)
            print(f"✓ Checking Account '{acc_num}' created successfully!")
        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.")
    
    elif choice == "3":
        # Deposit Money
        acc_num = input("Enter account number: ").strip()
        if acc_num in accounts:
            try:
                amount = int(float(input("Enter deposit amount: $")))
                accounts[acc_num].deposit(amount)
            except ValueError:
                print("❌ Invalid amount. Please enter a valid number.")
        else:
            print(f"❌ Account '{acc_num}' not found.")
    
    elif choice == "4":
        # Withdraw Money
        acc_num = input("Enter account number: ").strip()
        if acc_num in accounts:
            try:
                amount = int(float(input("Enter withdrawal amount: $")))
                accounts[acc_num].withdraw(amount)
            except ValueError:
                print("❌ Invalid amount. Please enter a valid number.")
        else:
            print(f"❌ Account '{acc_num}' not found.")
    
    elif choice == "5":
        # View Account Info
        acc_num = input("Enter account number: ").strip()
        if acc_num in accounts:
            accounts[acc_num].display_info()
        else:
            print(f"❌ Account '{acc_num}' not found.")
    
    elif choice == "6":
        # Add Interest (Savings Account)
        acc_num = input("Enter account number: ").strip()
        if acc_num in accounts:
            if isinstance(accounts[acc_num], SavingsAccount):
                accounts[acc_num].add_interest()
            else:
                print("❌ Interest can only be added to Savings Accounts.")
        else:
            print(f"❌ Account '{acc_num}' not found.")
    
    elif choice == "7":
        # Exit
        print("\n" + "="*50)
        print("Thank you for using the Banking System!")
        print("="*50 + "\n")
        break
    
    else:
        print("❌ Invalid choice. Please enter a number between 1 and 7.")
