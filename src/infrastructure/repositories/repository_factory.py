from sqlalchemy.orm import sessionmaker, scoped_session

from domain.repository_interfaces.account import AccountRepository
from domain.repository_interfaces.customer import CustomerRepository
from domain.repository_interfaces.transaction import TransactionRepository
from infrastructure.repositories.postgres import BaseModel, engine
from infrastructure.repositories.postgres.account import PostgresAccountRepository
from infrastructure.repositories.postgres.customer import PostgresCustomerRepository
from infrastructure.repositories.postgres.transaction import PostgresTransactionRepository
from config.config import settings


class RepositoryFactory(object):
    _account_repo: AccountRepository = None
    _transaction_repo: TransactionRepository = None
    _customer_repo: CustomerRepository = None

    def __init__(self):
        if settings.DB_TYPE == "postgresql":
            BaseModel.metadata.create_all(engine)
            self.session = scoped_session(sessionmaker(bind=engine))
            self._account_repo = PostgresAccountRepository(self.session)
            self._transaction_repo = PostgresTransactionRepository(self.session)
            self._customer_repo = PostgresCustomerRepository(self.session)
        elif settings.DB_TYPE == "mysql":
            pass
            # TODO: implement later base on repositories/base/*
        else:
            raise Exception("DB_TYPE not supported")

    def account_repo(self) -> AccountRepository:
        return self._account_repo

    def transaction_repo(self) -> TransactionRepository:
        return self._transaction_repo

    def customer_repo(self) -> CustomerRepository:
        return self._customer_repo
