from ..models.user_model import User
from .. import db

class UserService:
    def list_users(self):
        return [user.to_dict() for user in User.query.all()]

    def create_user(self, name, email):
        if self._get_user_by_email(email):
            raise ValueError("Email já cadastrado")
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        
    def delete_user(self, id):
        user = User.query.get(id)
        if not user:
            raise ValueError("Usuário não encontrado")
        db.session.delete(user)
        db.session.commit()
        
    def update_user(self, id, name, email):
        user = User.query.get(id)
        if not user:
            raise ValueError("Usuário não encontrado")
        if email and self._get_user_by_email(email):
            raise ValueError("Email já cadastrado")
        user.name = name
        user.email = email
        db.session.commit()
        
    def _get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()
