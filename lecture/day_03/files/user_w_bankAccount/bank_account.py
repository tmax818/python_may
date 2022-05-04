class BankAccount:

    def __init__(self, interest_rate=.01, balance=0) -> None:
        self.interest_rate = interest_rate
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawl(self, amount):
        self.balance -= amount
        return self


    def display_balance(self):
        print(f"the current balance is: {self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance * self.interest_rate + self.balance
        return self

account = BankAccount()