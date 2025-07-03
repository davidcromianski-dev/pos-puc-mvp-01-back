from ..controller_interface import ControllerInterface
from ...services.expense_service import ExpenseService

class ExpenseController(ControllerInterface):
    def __init__(self):
        service = ExpenseService()
        super().__init__(
            service=service,
            domain='expenses',
            name=__name__,
            url_prefix='/expenses'
        )

expense_controller = ExpenseController()
expense_bp = expense_controller.blueprint
expense_url_prefix = expense_controller.url_prefix
