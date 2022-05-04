
from bank_account import BankAccount
class User:

    def __init__(self, name, email, account = {"savings":BankAccount(), "checking": BankAccount()}):
        self.name = name
        self.email = email
        self.account = account


    def deposit(self, amount, acct_type='savings'):
        self.account[acct_type].make_deposit(amount)
    

    def withdrawl(self, amount, acct_type='checking'):
        self.account[acct_type].make_withdrawl(amount)

    def display_user_balance(self):
        print(f"{self.name},")
        self.account.display_balance()

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

bankaccount1 = BankAccount()
bankaccount2 = BankAccount()

user1 = User('yo han', "email.com", bankaccount1)
user2 = User('davita', "email.com")

