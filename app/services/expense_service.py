from .service_interface import ServiceInterface
from ..models.expense_model import Expense
from ..models.model_interface import ModelInterface
from typing import Any, Dict

class ExpenseService(ServiceInterface):
    """
    Service to manipulate the Expense domain
    """
    
    _model = Expense
    
    def create(self, data: Dict[str, Any]) -> ModelInterface:
        if (data['actual_date']):
            data['actual_date'] = super().handle_date(data['actual_date'])

        if(data['expected_date']):
           data['expected_date'] = super().handle_date(data['expected_date'])

        return super().create(data)