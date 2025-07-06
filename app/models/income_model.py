from sqlalchemy import func, Enum, Column, Integer, Float, String, Date, DateTime, ForeignKey
from .abstract_model import AbstractModel

"""
This module defines the Income model, representing a financial income record in the system.
"""

class Income(AbstractModel):
    """
    Represents an Income, an amount of money that has been or will be received.

    Attributes:
        id (int): The unique ID for this income.
        amount (float): The amount of money to be received.
        description (str): An explanation of this income.
        category (str): The income's category.
        account_id (int): The ID of the account associated with this income.
        income_type (str): The type of income (e.g., salary, bonus).
        payment_method (str): The method of payment for this income.
        expected_date (datetime.date): The expected date for the income to be received.
        actual_date (datetime.date): The actual date the income was received.
        status (str): The status of the income (PE=Pending, RE=Received, OD=Overdue, CA=Cancelled).
        created_at (datetime): The timestamp when the income was created.
    """
    __tablename__ = 'incomes'
    
    id = Column(Integer, primary_key=True)
    amount = Column(Float(precision=2), nullable=False)
    description = Column(String(120), nullable=False)
    category = Column(String(120), nullable=False)
    # Foreign Key for table `accounts`
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=True)
    income_type = Column(String(120), nullable=False)
    payment_method = Column(String(120), nullable=False)
    expected_date = Column(Date, nullable=False)
    actual_date = Column(Date, nullable=False)
    # PE = Pending, RE = Received, OD = Overdue, CA = Cancelled
    status = Column(Enum('PE', 'RE', 'OD', 'CA', name='expense_status'), nullable=False, default='PE')
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the Income instance, showing the amount.
        Returns:
            str: String representation of the Income.
        """
        return f'<Income {self.amount}>'

    def to_dict(self):
        """
        Converts the Income instance into a dictionary.
        Returns:
            dict: A dictionary containing the income's data.
        """
        return {
            "id": self.id,
            "amount": self.amount,
            "description": self.description,
            "category": self.category,
            "account_id": self.account_id,
            "income_type": self.income_type,
            "payment_method": self.payment_method,
            "expected_date": self.expected_date,
            "actual_date": self.actual_date,
            "status": self.status,
            "created_at": self.created_at,
        }
