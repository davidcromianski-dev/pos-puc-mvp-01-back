from pydantic import BaseModel
from typing import Optional, List
from ..models.expense_model import Expense
from enum import Enum

# ==== READ ====

def show_expense(expense: Expense):
    return {
        "id": expense.id,
        "amount": expense.amount,
        "description": expense.description,
        "category": expense.category,
        "account_id": expense.account_id,
        "expense_type": expense.expense_type,
        "payment_method": expense.payment_method,
        "expected_date": expense.expected_date,
        "actual_date": expense.actual_date,
        "status": expense.status,
        "created_at": expense.created_at,
    }

class ExpenseStatusEnum(str, Enum):
    PE = 'PE'  # Pending
    PA = 'PA'  # Paid
    OD = 'OD'  # Overdue
    CA = 'CA'  # Cancelled

class ExpenseSchema(BaseModel):
    id: int
    amount: float
    description: str
    category: str
    account_id: Optional[int]
    expense_type: str
    payment_method: str
    expected_date: Optional[str]
    actual_date: Optional[str]
    status: ExpenseStatusEnum
    created_at: str

class ExpenseResponseSchema(BaseModel):
    data: ExpenseSchema

def show_expenses(expenses: List[Expense]):
    result = []
    for expense in expenses:
        result.append(show_expense(expense))
    return {"expenses": result}

class ExpensesResponseSchema(BaseModel):
    data: List[ExpenseSchema]

# ==== CREATE ====

class ExpenseCreateSchema(BaseModel):
    amount: float
    description: str
    category: str
    account_id: Optional[int]
    expense_type: str
    payment_method: str
    expected_date: Optional[str]
    actual_date: Optional[str]
    status: Optional[ExpenseStatusEnum] = ExpenseStatusEnum.PE

# ==== UPDATE ====

class ExpenseUpdateSchema(BaseModel):
    amount: Optional[float]
    description: Optional[str]
    category: Optional[str]
    account_id: Optional[int]
    expense_type: Optional[str]
    payment_method: Optional[str]
    expected_date: Optional[str]
    actual_date: Optional[str]
    status: Optional[ExpenseStatusEnum]

class ExpenseUpdateResponseSchema(BaseModel):
    id: int
    message: str

# ==== DELETE ====

class ExpenseDeleteResponseSchema(BaseModel):
    id: int
    message: str
