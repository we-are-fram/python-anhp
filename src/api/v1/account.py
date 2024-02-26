from fastapi import APIRouter

from infrastructure.repositories.repository_factory import RepositoryFactory
from use_case.account import AccountUseCase
from use_case.transaction import TransactionUseCase
from domain.entities.transaction import TransactionType
from domain.entities.account import Account
from domain.entities.transaction import Transaction

router = APIRouter()
repository = RepositoryFactory()

account_usecase = AccountUseCase(
    account_repo=repository.account_repo(),
    customer_repo=repository.customer_repo(),
    transaction_repo=repository.transaction_repo(),
)

transaction_usecase = TransactionUseCase(
    account_repo=repository.account_repo(),
    transaction_repo=repository.transaction_repo(),
)


@router.post("/accounts")
def create_account(customer_id: int) -> Account:
    account = account_usecase.create_account(customer_id=customer_id)
    return account


@router.get("/accounts/{account_id}")
def get_account(account_id: int) -> Account:
    account = account_usecase.find_account_by_id(account_id=account_id)
    return account


@router.post("/accounts/{account_id}/deposit")
def deposit(account_id: int, amount: float) -> Transaction:
    transaction = transaction_usecase.make_transaction(
        account_id=account_id, amount=amount, transaction_type=TransactionType.DEPOSIT
    )
    return transaction


@router.post("/accounts/{account_id}/withdraw")
def withdraw(account_id: int, amount: float) -> Transaction:
    transaction = transaction_usecase.make_transaction(
        account_id=account_id, amount=amount, transaction_type=TransactionType.WITHDRAW
    )
    return transaction


@router.get("/accounts/{account_id}/statement")
def get_statement(account_id: int) -> list[Transaction]:
    statement = account_usecase.generate_account_statement(account_id=account_id)
    return statement
