# Account

class Account:
    def __init__(self, number: int, owner: str, balance: float, limit: float):
        self.number = number
        self.owner = owner
        self.balance = balance
        self.limit = limit

    def show_extract(self):
        print(self.balance)

    def deposit(self, value: float):
        self.balance += value

    def withdraw(self, value: float):
        self.balance -= value


kaike_account = Account(1233, 'Kaike Cesar Oliveira', 1305.90, 230.00)
kaike_account.show_extract()
kaike_account.deposit(240.98)
kaike_account.show_extract()
