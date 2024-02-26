from datetime import datetime
from enum import Enum
from pydantic import BaseModel, ConfigDict


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


class Transaction(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int = None
    account_id: int
    type: TransactionType
    amount: float
    created_at: datetime = datetime.now()
