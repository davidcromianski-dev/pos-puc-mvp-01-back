from flask import redirect
from flask_cors import CORS
from flask_openapi3.openapi import OpenAPI
from flask_openapi3.models.info import Info
from flask_openapi3.models.tag import Tag

from .extensions import db, migrate
from .controllers import AccountController, ExpenseController, IncomeController

def create_app(config_class):
    info = Info(title="API de controle fincanceiro - MVP", version="1.0.0")
    app = OpenAPI(__name__, info=info)
    app.config.from_object(config_class)
    
    CORS(app)
    
    db.init_app(app)
    migrate.init_app(app, db)

    home_tag = Tag(name="Home", description="Rota raiz da API")
    @app.get('/', tags=[home_tag])
    def home():
        """
        Redireciona para /openapi para o usuário escolher o estilo de documentação
        """
        return redirect('/openapi')
    
    controllers = [
        AccountController,
        ExpenseController,
        IncomeController
    ]
    
    for controller in controllers:
        controller(app).register()
        
    #print('Registered routes:')
    #for rule in app.url_map.iter_rules():
    #    print(rule, rule.methods)

    return app
