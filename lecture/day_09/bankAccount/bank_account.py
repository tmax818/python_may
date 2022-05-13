class BankAccount:
    
    def __init__(self, balance) -> None:
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def show_bal(self):
        print(self.balance)