from flask import Blueprint, request, jsonify
from ..services.user_service import UserService

bp = Blueprint('users', __name__, url_prefix='/users')
service = UserService()

@bp.route('/', methods=['GET'])
def list_users():
    """
    Lista os usuários
    ---
    responses:
      200:
        description: Lista de usuários
    """
    return jsonify(service.list_users())

@bp.route('/', methods=['POST'])
def create_user():
    """
    Cria um usuário
    ---
    parameters:
      - name: name
        in: formData
        type: string
        required: true
      - name: email
        in: formData
        type: string
        required: true
    responses:
      201:
        description: Usuário criado
    """
    try:
        name = request.form['name']
        email = request.form['email']
        id = service.create_user(name, email)
        return jsonify({"message": "Usuário criado", "id": id}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    """
    Deleta um usuário
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Usuário deletado
      404:
        description: Usuário não encontrado
    """
    try:
        service.delete_user(id)
        return jsonify({"message": "Usuário deletado", "id": id}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    """
    Atualiza um usuário
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: name
        in: formData
        type: string
        required: false
      - name: email
        in: formData
        type: string
        required: false
    responses:
      200:
        description: Usuário atualizado
      404:
        description: Usuário não encontrado
    """
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        service.update_user(id, name, email)
        return jsonify({"message": "Usuário atualizado", "id": id}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
