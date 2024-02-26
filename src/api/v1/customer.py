from fastapi import APIRouter

from domain.entities.customer import Customer
from infrastructure.repositories.repository_factory import RepositoryFactory
from use_case.customer import CustomerUseCase

router = APIRouter()
repository = RepositoryFactory()

customer_usecase = CustomerUseCase(
    customer_repo=repository.customer_repo(),
)


@router.post("/customers")
def create_customer(customer: Customer) -> Customer:
    customer = customer_usecase.create(
        name=customer.name, email=customer.email, phone_number=customer.phone_number
    )
    return customer


@router.get("/customers/{customer_id}")
def get(customer_id: int) -> Customer:
    customer = customer_usecase.get(customer_id=customer_id)
    return customer
