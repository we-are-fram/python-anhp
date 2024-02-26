from abc import ABC, abstractmethod
from typing import Any

from domain.entities.account import Account


class AccountRepository(ABC):
    session: Any

    @abstractmethod
    def create(self, account: Account) -> Account:
        raise NotImplementedError

    @abstractmethod
    def get(self, account_id: int) -> Account:
        raise NotImplementedError

    @abstractmethod
    def find_accounts_by_customer_id(self, customer_id) -> Account:
        raise NotImplementedError

    @abstractmethod
    def update(self, account) -> Account:
        raise NotImplementedError
