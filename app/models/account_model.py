from sqlalchemy import func, Column, Integer, String, DateTime, Boolean
from .abstract_model import AbstractModel

"""
This module defines the Account model, representing a bank account in the system.
"""

class Account(AbstractModel):
    """
    Represents a bank account used for tracking financial transactions.

    Attributes:
        id (int): The unique ID for this account.
        bank (str): The name of the bank where the account is held.
        active (bool): Indicates if the account is active.
        created_at (datetime): The timestamp when the account was created.
    """
    __tablename__ = 'accounts'
    
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True)
    bank = Column(String(120), nullable=False)
    # May be added futher, but due to security risks, I will not implement this now
    #branch_number = Column(String(120), nullable=False)
    #account_number = Column(String(120), nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the Account instance, showing the ID and bank name.
        Returns:
            str: String representation of the Account.
        """
        return f'<Account {self.id} - {self.bank}>'

    def to_dict(self):
        """
        Converts the Account instance into a dictionary.
        Returns:
            dict: A dictionary containing the account's data.
        """
        return {
            "id": self.id,
            "bank": self.bank,
            #"branch_number": self.branch_number,
            #"account_number": self.account_number,
            "active": self.active,
            "created_at": self.created_at,
        }
