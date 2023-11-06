# Account

class Account:
    def __init__(self, number: int, owner: str, balance: float, limit: float):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def show_account_details(self):
        print(self.__dict__)

    def show_extract(self):
        print(self.__balance)

    def deposit(self, value: float):
        self.__balance += value

    def withdraw(self, value: float):
        limit = self.__balance + self.__limit
        if limit <= 0 and value > limit:
            print('Sorry you cannot withdraw money! Because you do not have balance')
        else:
            self.__balance -= value

    def transfer(self, value: float, target):
        self.withdraw(value)
        target.deposit(value)


account_1 = Account(1233, 'Kaike Cesar Oliveira', 1305.90, 230.00)
account_2 = Account(321, 'Jonas', 00.00, 00.00)
account_1.transfer(1200.00, account_2)
