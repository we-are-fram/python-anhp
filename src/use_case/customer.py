from domain.entities.customer import Customer
from domain.repository_interfaces.customer import CustomerRepository
from use_case.common import exceptions


class CustomerUseCase(object):
    customer_repo: CustomerRepository

    def __init__(self, customer_repo: CustomerRepository):
        self.customer_repo = customer_repo

    def create(self, name: str, email: str, phone_number: str):
        customer = Customer(name=name, email=email, phone_number=phone_number)
        return self.customer_repo.create(customer)

    def get(self, customer_id):
        customer = self.customer_repo.get(customer_id)
        if not customer:
            raise exceptions.ErrorCustomerNotFound
        return customer
