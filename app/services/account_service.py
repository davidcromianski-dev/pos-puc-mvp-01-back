from .abstract_service import AbstractService
from ..models.account_model import Account

class AccountService(AbstractService):
    
    """
    Service to manipulate the Account domain
    """
    
    _model = Account