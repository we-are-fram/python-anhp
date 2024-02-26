from typing import List

from sqlalchemy.orm import Session

from domain.entities.transaction import Transaction
from domain.repository_interfaces.transaction import TransactionRepository
from infrastructure.repositories.postgres.models.transaction import TransactionModel


class PostgresTransactionRepository(TransactionRepository):
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def create(self, transaction: Transaction) -> Transaction:
        transaction_model = TransactionModel(
            id=transaction.id,
            account_id=transaction.account_id,
            amount=transaction.amount,
            type=transaction.type.value,
            created_at=transaction.created_at,
        )
        self.session.add(transaction_model)
        self.session.commit()
        self.session.refresh(transaction_model)
        return Transaction.model_validate(transaction_model)

    def list_by_account_id(self, account_id: int) -> List[Transaction]:
        transaction_models = (
            self.session.query(TransactionModel)
            .filter(TransactionModel.account_id == account_id)
            .order_by(TransactionModel.created_at.desc())
            .all()
        )
        return [Transaction.model_validate(model) for model in transaction_models]
