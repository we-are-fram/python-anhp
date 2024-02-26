import pytest
from use_case.common import exceptions
from use_case.account import AccountUseCase
from use_case.customer import CustomerUseCase
from use_case.transaction import TransactionUseCase
from domain.entities.transaction import TransactionType


def test_create_account_successfully(
    account_use_case: AccountUseCase, customer_use_case: CustomerUseCase
):
    created_customer = customer_use_case.create(
        name="Edmund",
        email="edmund@gmail.com",
        phone_number="123456789",
    )
    created_account = account_use_case.create_account(customer_id=created_customer.id)
    assert created_account.id is not None
    assert created_account.account_number is not None
    assert created_account.customer_id == created_customer.id
    assert created_account.balance == 0


def test_create_account_with_unknown_customer_id(account_use_case: AccountUseCase):
    with pytest.raises(exceptions.ErrorCustomerNotFound):
        unknown_customer_id = 999
        account_use_case.create_account(customer_id=unknown_customer_id)


def test_find_account_by_id(account_use_case: AccountUseCase, customer_use_case: CustomerUseCase):
    created_customer = customer_use_case.create(
        name="Edmund",
        email="edmund@gmail.com",
        phone_number="123456789",
    )
    created_account = account_use_case.create_account(customer_id=created_customer.id)

    account_use_case.find_account_by_id(account_id=created_account.id)
    assert created_account.id is not None
    assert created_account.account_number is not None
    assert created_account.customer_id == created_customer.id
    assert created_account.balance == 0


def test_find_account_by_customer_id(
    account_use_case: AccountUseCase, customer_use_case: CustomerUseCase
):
    created_customer = customer_use_case.create(
        name="Edmund",
        email="edmund@gmail.com",
        phone_number="123456789",
    )
    account_use_case.create_account(customer_id=created_customer.id)
    account_use_case.create_account(customer_id=created_customer.id)

    accounts = account_use_case.find_accounts_by_customer_id(customer_id=created_customer.id)
    assert len(accounts) == 2


def test_generate_account_statement(
    account_use_case: AccountUseCase, customer_use_case: CustomerUseCase, transaction_use_case: TransactionUseCase
):
    created_customer = customer_use_case.create(
        name="Edmund",
        email="edmund@gmail.com",
        phone_number="123456789",
    )
    created_account = account_use_case.create_account(customer_id=created_customer.id)
    transaction_use_case.make_transaction(
        account_id=created_account.id, amount=100, transaction_type=TransactionType.DEPOSIT
    )
    transaction_use_case.make_transaction(
        account_id=created_account.id, amount=50, transaction_type=TransactionType.WITHDRAW
    )

    transactions = account_use_case.generate_account_statement(account_id=created_account.id)
    assert len(transactions) == 2
