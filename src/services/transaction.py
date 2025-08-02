from databases.interfaces import Record

from src.schemas.transaction import TransactionIn
from src.models.transaction import transactions
from src.database import database
from src.exceptions import (
    NotFoundTransactionError,
    NotFoundAccountError,
    InvalidAmountError,
    InsufficientBalanceError,
    InvalidTransactionTypeError,
)
from datetime import datetime
from src.models.account import accounts


class TransactionService:
    async def read_all(self, limit: int = 10, skip: int = 0) -> list[Record]:
        query = transactions.select().limit(limit).offset(skip)
        return await database.fetch_all(query)

    async def read(self, id: int) -> Record:
        return await self.__get_by_id(id)

    async def create(self, transaction: TransactionIn) -> Record:
        # Search for account
        query = accounts.select().where(accounts.c.id == transaction.account_id)
        account = await database.fetch_one(query)
        if not account:
            raise NotFoundAccountError

        # Validate transaction type and amount
        if transaction.transaction_type not in ["withdrawal", "deposit"]:
            raise InvalidTransactionTypeError
        if transaction.amount <= 0:
            raise InvalidAmountError

        # Validate withdrawal conditions
        if transaction.transaction_type == "withdrawal":
            if transaction.amount > account.balance:
                raise InsufficientBalanceError

        # Calculate new balance
        new_balance = (
            account.balance - transaction.amount
            if transaction.transaction_type == "withdrawal"
            else account.balance + transaction.amount
        )

        # Update account balance
        update_query = (
            accounts.update()
            .where(accounts.c.id == transaction.account_id)
            .values(balance=new_balance)
        )
        await database.execute(update_query)

        # Create transaction record
        transaction_data = self.__create_transaction_data(transaction)
        query = transactions.insert().values(**transaction_data)
        transaction_id = await database.execute(query)

        # Return created transaction
        return await self.__get_by_id(transaction_id)

    def __create_transaction_data(self, transaction: TransactionIn) -> dict:
        now = datetime.now()
        return {
            "account_id": transaction.account_id,
            "amount": transaction.amount,
            "transaction_type": transaction.transaction_type,
            "published_at": now,
        }

    async def __get_by_id(self, id: int) -> Record:
        query = transactions.select().where(transactions.c.id == id)
        transaction = await database.fetch_one(query)
        if not transaction:
            raise NotFoundTransactionError
        return transaction
