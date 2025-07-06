from pydantic import BaseModel
from typing import Optional, List
from ..models.income_model import Income
from enum import Enum

# ==== READ ====

def show_income(income: Income):
    return {
        "id": income.id,
        "amount": income.amount,
        "description": income.description,
        "category": income.category,
        "account_id": income.account_id,
        "income_type": income.income_type,
        "payment_method": income.payment_method,
        "expected_date": income.expected_date,
        "actual_date": income.actual_date,
        "status": income.status,
        "created_at": income.created_at,
    }

class IncomeStatusEnum(str, Enum):
    PE = 'PE'  # Pending
    RE = 'RE'  # Received
    OD = 'OD'  # Overdue
    CA = 'CA'  # Cancelled

class IncomeSchema(BaseModel):
    id: int
    amount: float
    description: str
    category: str
    account_id: Optional[int]
    income_type: str
    payment_method: str
    expected_date: str
    actual_date: str
    status: IncomeStatusEnum
    created_at: str

class IncomeResponseSchema(BaseModel):
    data: IncomeSchema

def show_incomes(incomes: List[Income]):
    result = []
    for income in incomes:
        result.append(show_income(income))
    return {"incomes": result}

class IncomesResponseSchema(BaseModel):
    data: List[IncomeSchema]

# ==== CREATE ====

class IncomeCreateSchema(BaseModel):
    amount: float
    description: str
    category: str
    account_id: Optional[int]
    income_type: str
    payment_method: str
    expected_date: str
    actual_date: str
    status: Optional[IncomeStatusEnum] = IncomeStatusEnum.PE

# ==== UPDATE ====

class IncomeUpdateSchema(BaseModel):
    amount: Optional[float]
    description: Optional[str]
    category: Optional[str]
    account_id: Optional[int]
    income_type: Optional[str]
    payment_method: Optional[str]
    expected_date: Optional[str]
    actual_date: Optional[str]
    status: Optional[IncomeStatusEnum]

class IncomeUpdateResponseSchema(BaseModel):
    id: int
    message: str

# ==== DELETE ====

class IncomeDeleteResponseSchema(BaseModel):
    id: int
    message: str 