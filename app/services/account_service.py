from .service_interface import ServiceInterface
from ..models.account_model import Account

class AccountService(ServiceInterface):
    
    """
    Service to manipulate the Account domain
    """
    
    _model = Account