from sqlalchemy import Integer, String, Float, Column
from infrastructure.repositories.postgres import BaseModel


class AccountModel(BaseModel):
    __tablename__ = "account"

    id = Column("id", Integer, primary_key=True)
    customer_id = Column("customer_id", Integer)
    account_number = Column("account_number", String)
    balance = Column("balance", Float, default=0.0)
