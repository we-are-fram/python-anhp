class ErrorCustomerNotFound(Exception):

    def __init__(self, message="Customer not found"):
        self.message = message


class ErrorAccountNotFound(Exception):

    def __init__(self, message="Account not found"):
        self.message = message


class ErrorInsufficientBalance(Exception):

    def __init__(self, message="Insufficient balance"):
        self.message = message


class ErrorNotSupportTransactionType(Exception):

    def __init__(self, message="Not supported transaction type"):
        self.message = message
