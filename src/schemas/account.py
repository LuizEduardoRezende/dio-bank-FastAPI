from pydantic import BaseModel
from datetime import datetime


class AccountIn(BaseModel):
    account_number: str
    owner_name: str
    is_active: bool = True


class AccountUpdateIn(BaseModel):
    account_number: str | None = None
    owner_name: str | None = None
    is_active: bool | None = None
