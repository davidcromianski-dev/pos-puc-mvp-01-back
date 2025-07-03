from abc import ABC
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from ..services.service_interface import ServiceInterface

class ControllerInterface(ABC):
    
    _service: ServiceInterface
    
    _blueprint: Blueprint
    
    _domain: str
    
    _url_prefix: str
    
    def __init__(
        self,
        service: ServiceInterface,
        domain: str,
        name: str,
        url_prefix: str
    ):
        self._service = service
        self._domain = domain
        self._url_prefix = url_prefix
        self._set_blueprint(domain, name)
        self._register_routes()
    
    def _set_blueprint(self, domain: str, name: str):
        self._blueprint = Blueprint(domain, name)
    
    def _register_routes(self):  
        @self._blueprint.route('/', methods=['GET'])
        @swag_from(f'{self._url_prefix.lstrip("/")}/docs/list.yml')
        def list_models():
            try:
                return jsonify(self._service.list()), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        @self._blueprint.route('/', methods=['POST'])
        @swag_from(f'{self._url_prefix.lstrip("/")}/docs/create.yml')
        def create_model():
            try:
                data = request.get_json() or request.form.to_dict()
                new_instance = self._service.create(data)
                return jsonify({
                    "message": f"{self._service._model.__name__} created successfully",
                    "id": new_instance.id,
                    "data": new_instance.to_dict()
                }), 201
            except ValueError as e:
                return jsonify({"error": str(e)}), 400
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        @self._blueprint.route('/<int:id>', methods=['GET'])
        @swag_from(f'{self._url_prefix.lstrip("/")}/docs/get_one.yml')
        def get_model(id):
            try:
                instance = self._service.get_one_by_key(id)
                return jsonify(instance.to_dict()), 200
            except ValueError as e:
                return jsonify({"error": str(e)}), 404
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        @self._blueprint.route('/<int:id>', methods=['PUT'])
        @swag_from(f'{self._url_prefix.lstrip("/")}/docs/update.yml')
        def update_model(id):
            try:
                data = request.get_json() or request.form.to_dict()
                updated_instance = self._service.update(id, data)
                return jsonify({
                    "message": f"{self._service._model.__name__} updated successfully",
                    "id": updated_instance.id,
                    "data": updated_instance.to_dict()
                }), 200
            except ValueError as e:
                return jsonify({"error": str(e)}), 404
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        @self._blueprint.route('/<int:id>', methods=['DELETE'])
        @swag_from(f'{self._url_prefix.lstrip("/")}/docs/delete.yml')
        def delete_model(id):
            try:
                self._service.delete(id)
                return jsonify({
                    "message": f"{self._service._model.__name__} deleted successfully",
                    "id": id
                }), 200
            except ValueError as e:
                return jsonify({"error": str(e)}), 404
            except Exception as e:
                return jsonify({"error": str(e)}), 500
    
    @property
    def blueprint(self) -> Blueprint:
        """Get the blueprint instance"""
        return self._blueprint
    
    @property
    def url_prefix(self) -> str:
        """Get the url prefix"""
        return self._url_prefix
    