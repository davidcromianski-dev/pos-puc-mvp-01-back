from .abstract_service import AbstractService
from ..models.income_model import Income
from ..models.abstract_model import AbstractModel
from typing import Any, Dict

class IncomeService(AbstractService):
    """
    Service to manipulate the Income domain
    """
    
    _model = Income
    
    def create(self, data: Dict[str, Any]) -> AbstractModel:
        if (data['actual_date']):
            data['actual_date'] = super().handle_date(data['actual_date'])

        if(data['expected_date']):
           data['expected_date'] = super().handle_date(data['expected_date'])

        return super().create(data)
    
    def update(self, id: int, data: Dict[str, Any]) -> AbstractModel:
        if (data['actual_date']):
            data['actual_date'] = super().handle_date(data['actual_date'])

        if(data['expected_date']):
           data['expected_date'] = super().handle_date(data['expected_date'])

        return super().update(id, data)