from domain.entities.transaction import Transaction, TransactionType
from domain.repository_interfaces.account import AccountRepository
from domain.repository_interfaces.transaction import TransactionRepository
from use_case.common import exceptions


class TransactionUseCase(object):
    transaction_repo: TransactionRepository
    account_repo: AccountRepository

    def __init__(self, transaction_repo: TransactionRepository, account_repo: AccountRepository):
        self.transaction_repo = transaction_repo
        self.account_repo = account_repo

    def make_transaction(
        self, account_id: int, amount: float, transaction_type: TransactionType
    ) -> Transaction:
        account = self.account_repo.get(account_id=account_id)
        if not account:
            raise exceptions.ErrorAccountNotFound()

        if transaction_type == TransactionType.WITHDRAW:
            if account.balance < amount:
                raise exceptions.ErrorInsufficientBalance()

        if transaction_type == TransactionType.DEPOSIT:
            account.deposit(amount=amount)
        elif transaction_type == TransactionType.WITHDRAW:
            account.withdraw(amount=amount)
        else:
            raise exceptions.ErrorNotSupportTransactionType()

        self.account_repo.update(account=account)
        transaction = Transaction(account_id=account_id, amount=amount, type=transaction_type)
        return self.transaction_repo.create(transaction)
