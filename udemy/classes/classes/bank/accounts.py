# Imports
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(
        self,
        branch: str,
        number: int,
        balance: float = 0
    ):

        self._branch = branch
        self._number = number
        self._balance = balance

    @abstractmethod
    def withdraw(self, value: float) -> float: ...

    def deposit(self, value: float) -> float:
        self._balance += value
        print(f'Your current balance is: ${self._balance:.2f}')
        return self._balance

    def extract(self) -> float:
        return self._balance

    def details(self):
        print(f'Your balance is: ${self._balance:.2f}')


class CurrentAccount(Account):
    def __init__(
        self,
        branch: str,
        number: int,
        balance: float = 0,
        limit: float = 0
    ):

        super().__init__(branch, number, balance)
        self._limit = limit

    def withdraw(self, value: float):
        balance_withdrawed = (self._balance + self._limit) - value

        if balance_withdrawed >= 0:
            self._balance -= value
            self.details()
            return self._balance

        print('Unable to withdraw the desired amount!')


class SavingsAccount(Account):
    def withdraw(self, value: float):
        balance_withdrawed = self._balance - value

        if balance_withdrawed >= 0:
            self._balance -= value
            self.details()
            return self._balance

        print('Unable to withdraw the desired amount!')


if __name__ == '__main__':
    sa1 = SavingsAccount('001', 123, 0)
    sa1.deposit(123.00)
    sa1.withdraw(12.00)

    ca1 = CurrentAccount('001', 12, 0, 100)
    ca1.withdraw(100)
