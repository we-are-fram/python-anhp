import pytest
from use_case.common import exceptions
from use_case.account import AccountUseCase
from use_case.customer import CustomerUseCase
from use_case.transaction import TransactionUseCase
from domain.entities.transaction import TransactionType


def test_make_transaction_successfully(
    account_use_case: AccountUseCase,
    customer_use_case: CustomerUseCase,
    transaction_use_case: TransactionUseCase,
):
    created_customer = customer_use_case.create(
        name="Edmund",
        email="edmund@gmail.com",
        phone_number="123456789",
    )
    created_account = account_use_case.create_account(customer_id=created_customer.id)
    deposit_transaction = transaction_use_case.make_transaction(
        account_id=created_account.id, amount=100, transaction_type=TransactionType.DEPOSIT
    )
    assert deposit_transaction.account_id == created_account.id
    assert deposit_transaction.type == TransactionType.DEPOSIT
    assert deposit_transaction.amount == 100

    account = account_use_case.find_account_by_id(account_id=created_account.id)
    assert account.balance == 100

    withdraw_transaction = transaction_use_case.make_transaction(
        account_id=created_account.id, amount=50, transaction_type=TransactionType.WITHDRAW
    )
    assert withdraw_transaction.type == TransactionType.WITHDRAW
    assert withdraw_transaction.amount == 50
    assert withdraw_transaction.account_id == created_account.id
    account = account_use_case.find_account_by_id(account_id=created_account.id)
    assert account.balance == 50


def test_make_transaction_with_unknown_account(transaction_use_case: TransactionUseCase):
    unknown_account_id = 99
    with pytest.raises(exceptions.ErrorAccountNotFound):
        transaction_use_case.make_transaction(
            account_id=unknown_account_id, amount=100, transaction_type=TransactionType.DEPOSIT
        )
    with pytest.raises(exceptions.ErrorAccountNotFound):
        transaction_use_case.make_transaction(
            account_id=unknown_account_id, amount=100, transaction_type=TransactionType.WITHDRAW
        )


def test_withdraw_error_insufficient_balance(
    account_use_case: AccountUseCase,
    customer_use_case: CustomerUseCase,
    transaction_use_case: TransactionUseCase,
):
    created_customer = customer_use_case.create(
        name="Edmund",
        email="edmund@gmail.com",
        phone_number="123456789",
    )
    created_account = account_use_case.create_account(customer_id=created_customer.id)
    deposit_transaction = transaction_use_case.make_transaction(
        account_id=created_account.id, amount=100, transaction_type=TransactionType.DEPOSIT
    )
    with pytest.raises(exceptions.ErrorInsufficientBalance):
        withdraw_transaction = transaction_use_case.make_transaction(
            account_id=created_account.id, amount=500, transaction_type=TransactionType.WITHDRAW
        )
