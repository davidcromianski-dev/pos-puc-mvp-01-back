from .abstract_service import AbstractService
from ..models.expense_model import Expense
from ..models.abstract_model import AbstractModel
from typing import Any, Dict

class ExpenseService(AbstractService):
    """
    Service to manipulate the Expense domain
    """
    
    _model = Expense
    
    def create(self, data: Dict[str, Any]) -> AbstractModel:
        if (data['actual_date']):
            data['actual_date'] = super().handle_date(data['actual_date'])

        if(data['expected_date']):
           data['expected_date'] = super().handle_date(data['expected_date'])

        return super().create(data)