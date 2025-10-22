class BankAccount:

    def __init__(self, account_balance: float = 0.0):
        self.account_balance = account_balance

    def deposit(self, amount: float):
        self.account_balance += amount

    def withdraw(self, amount: float):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False 

    def display_balance(self):
        print(f"Current Balance: R{self.account_balance:.2f}")


    