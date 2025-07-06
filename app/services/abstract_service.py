from abc import ABC
from typing import Any, Dict, Type
from ..models.abstract_model import AbstractModel
from app.extensions import db
from datetime import datetime

class AbstractService(ABC):
    """
    Abstract base class that defines the interface for all Services.
    """
    _model: Type[AbstractModel]
        
    def _validate_id(self, id: int):
        """
        Validates a given ID before executing any other action
        
        Args:
            id (int): The primary key (ID) of the record to retrieve.
        
        Raises:
            ValueError: If the ID is invalid.
        """
        
        if not isinstance(id, int) or id <= 0:
            raise ValueError("ID must be a positive integer")
    
    def _validate_data(self, data: Dict[str, Any]):
        """
        Validates if the data is a non-empty dictionary
        
        Args:
            data (Dict[str, Any]): Dictionary containing the fields.
                                  Keys are field names, values are the new values.
            
        Raises:
            ValueError: If the data is invalid.
        """
        if not isinstance(data, dict) or not data:
            raise ValueError("Data must be a non-empty dictionary")
    
    def check_exists(self, model: Any) -> AbstractModel:
        """
        Validates that a model instance exists and is not None.
        
        Args:
            model: The model instance to check.
            
        Returns:
            The model instance if it exists.
            
        Raises:
            ValueError: If the model is None or doesn't exist.
        """
        if not model:
            raise ValueError("Model instance does not exists")
        return model
    
    def handle_date(self, dateString: str):
        return datetime.strptime(dateString, "%Y-%m-%d").date()
    
    def get_one_by_key(self, id: int) -> AbstractModel:
        """
        Retrieves a single record by its primary key (ID).
        
        Args:
            id (int): The primary key (ID) of the record to retrieve.
            
        Returns:
            The model instance if found, None otherwise.
            
        Raises:
            ValueError: If the ID is invalid or the record doesn't exist.
        """
        try:
            self._validate_id(id)
            record = db.session.query(self._model).get(id)
            
            return self.check_exists(record)
            
        except Exception as e:
            raise ValueError(f"Error retrieving record with ID {id}: {str(e)}")
    
    def list(self):
        """Retrieve all records."""
        return [instance.to_dict() for instance in self._model.query.all()]
    
    def create(self, data: Dict[str, Any]) -> AbstractModel:
        """
        Create a new record.
        
        Args:
            data (Dict[str, Any]): Dictionary containing the fields for the new record.
                                  Keys are field names, values are the field values.
        
        Returns:
            The newly created model instance.
            
        Raises:
            ValueError: If the data is invalid or creation fails.
        """
        try:
            self._validate_data(data)
            
            new_instance = self._model()
            
            for field, value in data.items():
                if hasattr(new_instance, field):
                    setattr(new_instance, field, value)
            
            db.session.add(new_instance)
            db.session.commit()
            
            db.session.refresh(new_instance)
            
            return new_instance
            
        except ValueError as e:
            raise e
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error creating new {self._model.__name__}: {str(e)}")
    
    def delete(self, id):
        """
        Delete a record.
        
        Args:
            id (int): The primary key (ID) of the record to retrieve.
        
        Raises:
            ValueError: If the ID is invalid, the record doesn't exist or if the element cannot be deleted.
        """
        try:
            instance = self.get_one_by_key(id)
            db.session.delete(instance)
            db.session.commit()
        except Exception as e:
            raise ValueError(f"Error deleting record with ID {id}: {str(e)}")
        
    def update(self, id: int, data: Dict[str, Any]) -> AbstractModel:
        """
        Update an existing record.
        
        Args:
            id (int): The primary key (ID) of the record to update.
            data (Dict[str, Any]): Dictionary containing the fields to update.
                                  Keys are field names, values are the new values.
        
        Returns:
            The updated model instance.
            
        Raises:
            ValueError: If the ID is invalid, the record doesn't exist, or update fails.
        """
        
        try:
            self._validate_data(data)
            instance = self.get_one_by_key(id)
            
            updated_fields = []
            
            for field, value in data.items():
                if hasattr(instance, field):
                    current_value = getattr(instance, field)
                    if current_value != value:
                        setattr(instance, field, value)
                        updated_fields.append(field)
            
            if updated_fields:
                db.session.commit()
            
            return instance
            
        except ValueError as e:
            raise e
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error updating record with ID {id}: {str(e)}")
