from pydantic import BaseModel
from typing import Optional, List
from ..models.account_model import Account

class AccountIdSchema(BaseModel):
    id: int

# ==== READ ====

def show_account(account: Account):
    return {
        "id": account.id,
        "bank": account.bank,
        "active": account.active,
        "created_at": account.created_at,
    }

class AccountSchema(BaseModel):
    id: int = 1
    bank: str = 'Nome do Banco'
    active: bool = True
    created_at: str = '2025-07-03 03:16:19'

class AccountResponseSchema(BaseModel):
    data: AccountSchema

def show_accounts(accounts: List[Account]):
    result = []
    for account in accounts:
        result.append({
            "id": account.id,
            "bank": account.bank,
            "active": account.active,
            "created_at": account.created_at
        })

    return {"accounts": result}

class AccountsResponseSchema(BaseModel):
    data: List[AccountSchema]

# ==== CREATE ====

class AccountCreateSchema(BaseModel):
    bank: str = 'Nome do Banco'
    active: Optional[bool] = True
    
class AccountCreateResponseSchema(BaseModel):
    id: int = 1

# ===== UPDATE ==== #

class AccountUpdateSchema(BaseModel):
    bank: Optional[str] = 'Nome do banco'
    active: Optional[bool] = True

class AccountUpdateResponseSchema(BaseModel):
    id: int
    message: str

# ==== DELETE ==== #

class AccountDeleteResponseSchema(BaseModel):
    id: int
    mesage: str
