- [1. Backend Exam](#1-backend-exam)
  - [1.1. Task Description](#11-task-description)
  - [1.2. Requirements](#12-requirements)
  - [1.3. Notes](#13-notes)
- [2. Project Structure](#2-project-structure)
- [3. Deployment](#3-deployment)
- [4. Usage](#4-usage)
- [5. Run tests](#5-run-tests)


# 1. Backend Exam

## 1.1. Task Description

You are developing a banking system application that follows the clean architecture principles. The system contains the following three layers: Domain, Use Case, and Infrastructure.

The Domain layer consists of the entities representing domain concepts such as Account, Transaction, and Customer. These entities have methods for performing specific operations related to their respective domains.

The Use Case layer contains the business logic of the application. It includes use cases like creating a new account, making a transaction, and generating account statements.

The Infrastructure layer deals with the interaction between the application and the outside world. It includes repositories for persisting data, external service integrations, and data access objects.

Your task is to implement a simplified version of the banking system application based on clean architecture. You need to create the necessary classes and methods following the clean architecture principles.

## 1.2. Requirements

1. Implement the Account entity class with the following attributes: account_id, customer_id, account_number, balance.

    a. It should have the following methods: deposit(), withdraw(), and get_balance().

2. Implement the Customer entity class with the following attributes: customer_id, name, email, and phone_number.

3. Implement a Use Case class for creating a new account. It should have a method named create_account() that takes customer_id, name, email, and phone_number as input and returns an Account object.

4. Implement a Use Case class for making a transaction. It should have a method named make_transaction() that takes account_id, amount, and transaction_type (either 'deposit' or 'withdraw') as input and updates the account balance accordingly.

5. Implement a Use Case class for generating account statements. It should have a method named generate_account_statement() that takes account_id as input and returns a statement string containing transaction details for the given account.

6. Implement an Infrastructure class named AccountRepository for persisting and retrieving account data. It should have methods like save_account(), find_account_by_id(), and find_accounts_by_customer_id().

7. Implement a simple test scenario that demonstrates the use of all the implemented classes and methods.

## 1.3. Notes

● You don't need to implement any specific data storage mechanisms. Just focus on the class design and method implementations as per clean architecture principles.

● You can assume the availability of any required external libraries or modules.

● You should provide the complete implementation for the problem, including the necessary classes and methods.

# 2. Project Structure

The project structure is as follows:

```
src
├── domain          : contain the entities and repository interfaces of the system
└── use_case        : contain the use cases of the system
├── infrastructure  : contain the implementation of the repository interfaces using postgresql and sqlalchemy
├── api             : contain the API endpoints of fastapi
├── config          : contain the config of the system
├── tests           : contain the unit test
```

# 3. Deployment 

**Requirements**

- Development environment: Ubuntu 22.04
- Python 3.10
- Docker version 25.0.3
- Docker Compose plugin

Then run the following command:

```shell
docker-compose up -d
```

# 4. Usage

You can access the API docs at http://localhost:8000/docs

# 5. Run tests

Create test db:

```shell
docker compose exec database createdb -U postgres test_db || :
```

To run the tests, run the following command:

```shell
docker compose exec api pytest -vv --capture=no
```

output sample of the test:

```shell
(.venv) ➜  banking-system git:(master) ✗ docker compose exec api pytest -vv --capture=no

============================================================================ test session starts ============================================================================
platform linux -- Python 3.10.13, pytest-8.0.1, pluggy-1.4.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /app
plugins: anyio-4.3.0
collected 11 items                                                                                                                                                          

tests/test_account_use_case.py::test_create_account_successfully PASSED
tests/test_account_use_case.py::test_create_account_with_unknown_customer_id PASSED
tests/test_account_use_case.py::test_find_account_by_id PASSED
tests/test_account_use_case.py::test_find_account_by_customer_id PASSED
tests/test_account_use_case.py::test_generate_account_statement PASSED
tests/test_customer_use_case.py::test_create_customer_successfull PASSED
tests/test_customer_use_case.py::test_get_customer_successfully PASSED
tests/test_customer_use_case.py::test_get_customer_not_found PASSED
tests/test_transaction_use_case.py::test_make_transaction_successfully PASSED
tests/test_transaction_use_case.py::test_make_transaction_with_unknown_account PASSED
tests/test_transaction_use_case.py::test_withdraw_error_insufficient_balance PASSED

============================================================================ 11 passed in 0.54s =============================================================================
(.venv) ➜  banking-system git:(master) ✗ 

```
