from sqlalchemy import Integer, String, Column
from infrastructure.repositories.postgres import BaseModel


class CustomerModel(BaseModel):
    __tablename__ = "customer"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    email = Column("email", String)
    phone_number = Column("phone_number", String)
