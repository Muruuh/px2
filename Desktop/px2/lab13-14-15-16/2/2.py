class BankAccount:
    def __init__(self, customer_name, account_number, balance=0.0):
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds"

    def close_account(self):
        self.balance = 0
        return "Account closed"

    def view_balance(self):
        return f"Дансны үлдэгдэл {self.customer_name}: ${self.balance}"


with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    for line in input_file:
        data = line.strip().split(',')
        if data[0] == 'Open':
            account = BankAccount(data[1], data[2])
            output_file.write(f"Account opened for {account.customer_name} with account number {account.account_number}\n")
        elif data[0] == 'Deposit':
            output_file.write(account.deposit(float(data[1])) + "\n")
        elif data[0] == 'Withdraw':
            output_file.write(account.withdraw(float(data[1])) + "\n")
        elif data[0] == 'Close':
            output_file.write(account.close_account() + "\n")
        elif data[0] == 'View':
            output_file.write(account.view_balance() + "\n")
