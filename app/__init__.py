from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flasgger import Swagger

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    CORS(app)
    
    db.init_app(app)
    migrate.init_app(app, db)
    Swagger(app)
    
    from .controllers.accounts.account_controller import account_bp, account_url_prefix
    from .controllers.expenses.expense_controller import expense_bp, expense_url_prefix
    from .controllers.incomes.income_controller import income_bp, income_url_prefix

    app.register_blueprint(account_bp, url_prefix=account_url_prefix)
    app.register_blueprint(expense_bp, url_prefix=expense_url_prefix)
    app.register_blueprint(income_bp, url_prefix=income_url_prefix)

    return app
