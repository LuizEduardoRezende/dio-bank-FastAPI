from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from enum import Enum


class TransactionType(str, Enum):
    WITHDRAWAL = "withdrawal"
    DEPOSIT = "deposit"


class TransactionOut(BaseModel):
    id: int
    account_id: int
    amount: Decimal
    transaction_type: TransactionType
    published_at: datetime
