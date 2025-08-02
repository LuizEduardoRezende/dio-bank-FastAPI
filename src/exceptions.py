from http import HTTPStatus


class NotFoundAccountError(Exception):
    def __init__(
        self,
        message: str = "Account not found",
        status_code: int = HTTPStatus.NOT_FOUND,
    ):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class NotFoundTransactionError(Exception):
    def __init__(
        self,
        message: str = "Transaction not found",
        status_code: int = HTTPStatus.NOT_FOUND,
    ):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class InvalidAmountError(Exception):
    def __init__(
        self,
        message: str = "Invalid withdrawal amount",
        status_code: int = HTTPStatus.BAD_REQUEST,
    ):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class InsufficientBalanceError(Exception):
    def __init__(
        self,
        message: str = "Insufficient balance for withdrawal",
        status_code: int = HTTPStatus.BAD_REQUEST,
    ):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class InvalidTransactionTypeError(Exception):
    def __init__(
        self,
        message: str = "Invalid transaction type",
        status_code: int = HTTPStatus.BAD_REQUEST,
    ):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
