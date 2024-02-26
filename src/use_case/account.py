import uuid

from domain.entities.account import Account
from domain.entities.transaction import Transaction
from domain.repository_interfaces.account import AccountRepository
from domain.repository_interfaces.customer import CustomerRepository
from domain.repository_interfaces.transaction import TransactionRepository
from use_case.common import exceptions


class AccountUseCase(object):
    account_repo: AccountRepository
    customer_repo: CustomerRepository
    transaction_repo: TransactionRepository

    def __init__(
        self,
        account_repo: AccountRepository,
        customer_repo: CustomerRepository,
        transaction_repo: TransactionRepository,
    ):
        self.account_repo = account_repo
        self.customer_repo = customer_repo
        self.transaction_repo = transaction_repo

    def create_account(self, customer_id: int) -> Account:
        customer = self.customer_repo.get(customer_id=customer_id)
        if not customer:
            raise exceptions.ErrorCustomerNotFound()
        account = Account(customer_id=customer.id, balance=0, account_number=str(uuid.uuid4()))
        return self.account_repo.create(account)

    def find_account_by_id(self, account_id: str) -> Account:
        account = self.account_repo.get(account_id=account_id)
        if not account:
            raise exceptions.ErrorAccountNotFound()
        return account

    def find_accounts_by_customer_id(self, customer_id: int) -> Account:
        customer = self.customer_repo.get(customer_id=customer_id)
        if not customer:
            raise exceptions.ErrorCustomerNotFound()
        return self.account_repo.find_accounts_by_customer_id(customer_id=customer_id)

    def generate_account_statement(self, account_id: int) -> list[Transaction]:
        account = self.account_repo.get(account_id=account_id)
        if not account:
            raise exceptions.ErrorAccountNotFound()
        transactions = self.transaction_repo.list_by_account_id(account_id=account_id)
        return transactions
