# Imports
import accounts
import people


class Bank:
    def __init__(
        self,
        branches: list[str] | None = None,
        customers: list[people.Person] | None = None,
        accounts: list[accounts.Account] | None = None,
    ):
        self.branches = branches or []
        self.customers = customers or []
        self.accounts = accounts or []

    def _validate_branch(self, account) -> bool:
        validate_result = False
        if account.branch in self.branches:
            validate_result = True
        return validate_result

    def _validate_customer(self, customer) -> bool:
        validate_result = False
        if customer in self.customers:
            validate_result = True
        return validate_result

    def _validate_account(self, account) -> bool:
        validate_result = False
        if account in self.accounts:
            validate_result = True
        return validate_result

    def authenticate(self, customer, account):
        return self._validate_account(account) and \
            self._validate_branch(account) and \
            self._validate_customer(customer)
