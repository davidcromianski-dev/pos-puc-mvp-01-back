from sqlalchemy import func, Enum, Column, Integer, Float, String, Date, DateTime, ForeignKey
from .abstract_model import AbstractModel

"""
This module defines the Expense model, representing a financial expense record in the system.
"""

class Expense(AbstractModel):
    
    """
    Represents an Expense, an amount of money that had been or will be deducted from an account.
    
    Attributes:
        id (int): The unique ID for this expense.
        amount (float): The amount of money to be deducted.
        description (str): An explanation of this expense.
        category (str): The expense's category.
        account_id (int): The ID of the account associated with this expense.
        expense_type (str): The type of expense (e.g., fixed, variable).
        payment_method (str): The method of payment used for this expense.
        expected_date (datetime.date): The expected date for the expense to occur.
        actual_date (datetime.date): The actual date the expense occurred.
        status (str): The status of the expense (PE=Pending, PA=Paid, OD=Overdue, CA=Cancelled).
        created_at (datetime): The timestamp when the expense was created.
    """
    
    __tablename__ = 'expenses'

    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True)
    amount = Column(Float(precision=2), nullable=False)
    description = Column(String(120), nullable=False)
    category = Column(String(120), nullable=False)
    # Foreign Key for table `accounts`
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=True)
    expense_type = Column(String(120), nullable=False)
    payment_method = Column(String(120), nullable=False)
    expected_date = Column(Date, nullable=True)
    actual_date = Column(Date, nullable=True)
    # PE = Pending, PA = Paid, OD = Overdue, CA = Cancelled
    status = Column(Enum('PE', 'PA', 'OD', 'CA', name='expense_status'), nullable=False, default='PE')
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the Expense instance, showing the amount.
        Returns:
            str: String representation of the Expense.
        """
        return f'<Expense {self.amount}>'

    def to_dict(self):
        """
        Converts the Expense instance into a dictionary.
        Returns:
            dict: A dictionary containing the expense's data.
        """
        return {
            "id": self.id,
            "amount": self.amount,
            "description": self.description,
            "category": self.category,
            "account_id": self.account_id,
            "expense_type": self.expense_type,
            "payment_method": self.payment_method,
            "expected_date": self.expected_date,
            "actual_date": self.actual_date,
            "status": self.status,
            "created_at": self.created_at,
        }
