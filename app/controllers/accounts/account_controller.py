from ..controller_interface import ControllerInterface
from ...services.account_service import AccountService

class AccountController(ControllerInterface):
    def __init__(self):
        service = AccountService()
        super().__init__(
            service=service,
            domain='accounts',
            name=__name__,
            url_prefix='/accounts'
        )

account_controller = AccountController()
account_bp = account_controller.blueprint
account_url_prefix = account_controller.url_prefix
