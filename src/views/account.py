from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal


class AccountOut(BaseModel):
    id: int
    account_number: str
    owner_name: str
    balance: Decimal
    is_active: bool
    created_at: datetime
    updated_at: datetime
