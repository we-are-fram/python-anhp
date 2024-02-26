from sqlalchemy import Integer, String, DateTime, Column
from infrastructure.repositories.postgres import BaseModel


class TransactionModel(BaseModel):
    __tablename__ = "transaction"

    id = Column("id", Integer, primary_key=True)
    account_id = Column("account_id", Integer)
    amount = Column("amount", Integer)
    type = Column("type", String)
    created_at = Column("created_at", DateTime)
