from typing import Optional

from sqlalchemy.orm import Session

from domain.entities.customer import Customer
from domain.repository_interfaces.customer import CustomerRepository
from infrastructure.repositories.postgres.models.customer import CustomerModel


class PostgresCustomerRepository(CustomerRepository):
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def create(self, customer: Customer) -> Customer:
        customer_model = CustomerModel(
            name=customer.name,
            email=customer.email,
            phone_number=customer.phone_number,
        )
        self.session.add(customer_model)
        self.session.commit()
        self.session.refresh(customer_model)
        return Customer.model_validate(customer_model)

    def get(self, customer_id: int) -> Optional[Customer]:
        customer_model = (
            self.session.query(CustomerModel).filter(CustomerModel.id == customer_id).first()
        )
        if customer_model is None:
            return None
        return Customer.model_validate(customer_model)
