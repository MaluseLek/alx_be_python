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
        print(f"Balance: R{self.account_balance}")


    """
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
    #     self.balance = balance

    # def deposit(self, amount: float) -> None:
    #     if amount <= 0:
    #         raise ValueError("Deposit amount must be positive.")
    #     self.balance += amount

    # def withdraw(self, amount: float) -> None:
    #     if amount <= 0:
    #         raise ValueError("Withdrawal amount must be positive.")
    #     if amount > self.balance:
    #         raise ValueError("Insufficient funds.")
    #     self.balance -= amount

    # def get_balance(self) -> float:
    #     return self.balance

    # def __str__(self) -> str:
    #     return f"Account {self.account_number} held by {self.account_holder} has a balance of ${self.balance:.2f}"

""" 