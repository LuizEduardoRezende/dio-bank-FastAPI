from databases.interfaces import Record
from datetime import datetime

from src.schemas.account import AccountIn
from src.schemas.account import AccountUpdateIn
from src.models.account import accounts
from src.models.transaction import transactions
from src.database import database
from src.exceptions import NotFoundAccountError


class AccountService:
    async def read_all(
        self, is_active: bool, limit: int = 10, skip: int = 0
    ) -> list[Record]:
        query = accounts.select().limit(limit).offset(skip)
        query = query.where(accounts.c.is_active == is_active)
        return await database.fetch_all(query)

    async def read(self, id: int) -> Record:
        return await self.__get_by_id(id)

    async def create(self, account: AccountIn) -> Record:
        now = datetime.now()
        command = accounts.insert().values(
            account_number=account.account_number,
            owner_name=account.owner_name,
            is_active=account.is_active,
            balance=0.00,
            created_at=now,
            updated_at=now,
        )
        account_id = await database.execute(command)
        return await self.__get_by_id(account_id)

    async def update(self, id: int, account: AccountUpdateIn) -> Record:

        await self.__get_by_id(id)

        data = account.model_dump(exclude_unset=True)
        data["updated_at"] = datetime.now()
        command = accounts.update().where(accounts.c.id == id).values(**data)
        await database.execute(command)

        return await self.__get_by_id(id)

    async def delete(self, id: int) -> None:

        await self.__get_by_id(id)

        command = accounts.delete().where(accounts.c.id == id)
        await database.execute(command)

    async def read_all_transactions(self, account_id: int) -> list[Record]:

        await self.__get_by_id(account_id)

        query = (
            transactions.select()
            .where(transactions.c.account_id == account_id)
            .order_by(transactions.c.published_at.desc())
        )
        return await database.fetch_all(query)

    async def __get_by_id(self, id: int) -> Record:
        query = accounts.select().where(accounts.c.id == id)
        account = await database.fetch_one(query)
        if not account:
            raise NotFoundAccountError
        return account
