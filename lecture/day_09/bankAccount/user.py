from bank_account import BankAccount

class User:
    
    def __init__(self, hair_length, bank_account) -> None:
        self.hair_length = hair_length
        self.bank_account = bank_account
        self.accounts = []

    def grow_hair(self):
        self.hair_length = "longer"

    def make_deposit(self, amt):
        self.bank_account.deposit(amt)

    def get_bal(self):
        self.bank_account.show_bal()

savings = BankAccount(500)
cesar = User("long", savings)