from .service_interface import ServiceInterface
from ..models.income_model import Income
from ..models.model_interface import ModelInterface
from typing import Any, Dict

class IncomeService(ServiceInterface):
    """
    Service to manipulate the Income domain
    """
    
    _model = Income
    
    def create(self, data: Dict[str, Any]) -> ModelInterface:
        if (data['actual_date']):
            data['actual_date'] = super().handle_date(data['actual_date'])

        if(data['expected_date']):
           data['expected_date'] = super().handle_date(data['expected_date'])

        return super().create(data)