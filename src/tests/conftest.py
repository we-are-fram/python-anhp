import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm.session import close_all_sessions

from config.config import settings
from infrastructure.repositories.postgres import BaseModel
from infrastructure.repositories.repository_factory import RepositoryFactory
from use_case.account import AccountUseCase
from use_case.customer import CustomerUseCase
from use_case.transaction import TransactionUseCase


@pytest.fixture(scope="function", autouse=True)
def reset_database_test():
    db_uri = f"{settings.DB_TYPE}://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/test_db"
    engine = create_engine(db_uri)
    conn = engine.connect()
    BaseModel.metadata.create_all(bind=engine)
    yield
    close_all_sessions()
    BaseModel.metadata.drop_all(bind=engine)
    conn.close()
    engine.dispose()


@pytest.fixture
def repository():
    return RepositoryFactory()


@pytest.fixture
def account_use_case(repository: RepositoryFactory):
    return AccountUseCase(
        account_repo=repository.account_repo(),
        customer_repo=repository.customer_repo(),
        transaction_repo=repository.transaction_repo()
    )


@pytest.fixture
def customer_use_case(repository: RepositoryFactory):
    return CustomerUseCase(customer_repo=repository.customer_repo())


@pytest.fixture
def transaction_use_case(repository: RepositoryFactory):
    return TransactionUseCase(
        account_repo=repository.account_repo(),
        transaction_repo=repository.transaction_repo()
    )