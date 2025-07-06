from abc import ABC, abstractmethod
from flask import Flask, request, jsonify
from flask_openapi3.models.tag import Tag
from ..services.abstract_service import AbstractService

class AbstractController(ABC):
    _app: Flask
    
    _service: type[AbstractService]
    
    _service_instance: AbstractService | None = None
    
    _domain: str
    
    _tag = Tag
    
    def __init__(
        self,
        app,
        service: type[AbstractService],
        domain: str,
        name: str,
    ):
        self._app = app
        self._service = service
        self._domain = domain
    
    @abstractmethod
    def register(self):
        pass
    
    def init_service(self) -> AbstractService:
        self._service_instance = self._service()
        return self._service_instance
        
    def service(self) -> AbstractService:
        if self._service_instance is not None and isinstance(self._service_instance, AbstractService):
            return self._service_instance
        return self.init_service()
    
    def list_models(self):
        try:
            return jsonify({"data": self.service().list()}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def create_model(self, body):
        try:
            data = body.dict()
            new_instance = self.service().create(data)
            return jsonify({
                "message": f"{self._service._model.__name__} created successfully",
                "id": new_instance.id,
                "data": new_instance.to_dict()
            }), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def get_model(self, id: int):
        try:
            instance = self.service().get_one_by_key(id)
            return jsonify({"data": instance.to_dict()}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def update_model(self, id: int, body):
        try:
            data = body.dict(exclude_unset=True)
            updated_instance = self.service().update(id, data)
            return jsonify({
                "message": f"{self._service._model.__name__} updated successfully",
                "id": updated_instance.id,
                "data": updated_instance.to_dict()
            }), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def delete_model(self, id: int):
        try:
            self.service().delete(id)
            return jsonify({
                "message": f"{self._service._model.__name__} deleted successfully",
                "id": id
            }), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        