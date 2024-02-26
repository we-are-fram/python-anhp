from typing import Optional
from sqlalchemy.orm import Session

from domain.entities.account import Account
from domain.repository_interfaces.account import AccountRepository
from infrastructure.repositories.postgres.models.account import AccountModel
from use_case.common import exceptions


class PostgresAccountRepository(AccountRepository):
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def create(self, account: Account) -> Account:
        account_model = AccountModel(
            id=account.id,
            customer_id=account.customer_id,
            account_number=account.account_number,
            balance=account.balance,
        )
        self.session.add(account_model)
        self.session.commit()
        self.session.refresh(account_model)
        return Account.model_validate(account_model)

    def get(self, account_id: int) -> Optional[Account]:
        account_model = (
            self.session.query(AccountModel).filter(AccountModel.id == account_id).first()
        )
        if account_model is None:
            return None
        return Account.model_validate(account_model)

    def update(self, account: Account) -> Account:
        account_model = (
            self.session.query(AccountModel).filter(AccountModel.id == account.id).first()
        )
        if account_model is None:
            raise exceptions.ErrorAccountNotFound()

        account_model.balance = account.balance
        account_model.customer_id = account.customer_id
        account_model.account_number = account.account_number
        self.session.merge(account_model)
        self.session.commit()
        self.session.refresh(account_model)
        return Account.model_validate(account_model)

    def find_accounts_by_customer_id(self, customer_id) -> Account:
        accounts = self.session.query(AccountModel).filter(AccountModel.customer_id == customer_id)
        return [Account.model_validate(account_model) for account_model in accounts]
