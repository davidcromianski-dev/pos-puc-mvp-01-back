from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    Swagger(app)

    from .controllers import user_controller
    app.register_blueprint(user_controller.bp)

    return app
