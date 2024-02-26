import pytest
from use_case.common import exceptions
from use_case.customer import CustomerUseCase


def test_create_customer_successfull(customer_use_case: CustomerUseCase):
    created_customer = customer_use_case.create(
        name="Edmund",
        email="edmund@gmail.com",
        phone_number="123456789",
    )
    assert created_customer.id is not None
    assert created_customer.name == "Edmund"
    assert created_customer.email == "edmund@gmail.com"
    assert created_customer.phone_number == "123456789"


def test_get_customer_successfully(customer_use_case: CustomerUseCase):
    created_customer = customer_use_case.create(
        name="Edmund",
        email="edmund@gmail.com",
        phone_number="123456789",
    )
    customer = customer_use_case.get(customer_id=created_customer.id)
    assert customer.id is not None
    assert customer.name == "Edmund"
    assert customer.email == "edmund@gmail.com"
    assert customer.phone_number == "123456789"


def test_get_customer_not_found(customer_use_case: CustomerUseCase):
    with pytest.raises(exceptions.ErrorCustomerNotFound):
        not_found_id = 999
        customer_use_case.get(customer_id=not_found_id)
