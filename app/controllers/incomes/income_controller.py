from ..controller_interface import ControllerInterface
from ...services.income_service import IncomeService

class IncomeController(ControllerInterface):
    def __init__(self):
        service = IncomeService()
        super().__init__(
            service=service,
            domain='incomes',
            name=__name__,
            url_prefix='/incomes'
        )

income_controller = IncomeController()
income_bp = income_controller.blueprint
income_url_prefix = income_controller.url_prefix