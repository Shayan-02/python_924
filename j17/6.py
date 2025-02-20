class BankAccount:
    def __init__(self, account_number, owner_name, balance=0, interest_rate=0.05):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdrew {amount}. New balance: {self.balance:}"
            else:
                return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def get_balance(self):
        return self.balance

    def display_info(self):
        return f"Account Number: {self.account_number}\nAccount Owner: {self.owner_name}\nAccount Owner: {self.owner_name}"


# Using the BankAccount class
account1 = BankAccount("1234567890", "John Smith")
print(account1.deposit(1000))
print(account1.withdraw(500))
print(account1.display_info())

account2 = BankAccount("9876543210", "Jane Doe", interest_rate=0.1)
print(account2.deposit(1500))
print(account2.withdraw(3000))
print(account2.display_info())
