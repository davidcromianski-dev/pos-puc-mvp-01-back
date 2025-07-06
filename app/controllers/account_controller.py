from .abstract_controller import AbstractController
from ..services.account_service import AccountService
from flask_openapi3.models.tag import Tag
from ..schemas.error import ErrorSchema
from ..schemas.generic import GenericIdSchema
from ..schemas.account_schema import AccountResponseSchema, AccountsResponseSchema, AccountUpdateResponseSchema, AccountDeleteResponseSchema, AccountCreateSchema, AccountUpdateSchema

class AccountController(AbstractController):
    def __init__(self, app):
        super().__init__(
            app,
            service=AccountService,
            domain='accounts',
            name=__name__,
        )
        self._tag = Tag(name="Contas", description="Adição, visualização e remoção de contas à base")
    
    def register(self):
        @self._app.get('/accounts', tags=[self._tag],
                       responses={"200": AccountsResponseSchema, "404": ErrorSchema})
        def list_accounts():
            """
            Lista todas as contas do sistema
            """
            return self.list_models()
        
        @self._app.get('/account', tags=[self._tag],
                       responses={"200": AccountResponseSchema, "404": ErrorSchema})
        def get_account(query: GenericIdSchema):
            """
            Lista uma conta de acordo com o ID informado
            """
            return self.get_model(query.id)
        
        @self._app.post('/account', tags=[self._tag],
                        responses={"201": AccountResponseSchema, "409": ErrorSchema, "400": ErrorSchema})
        def create_account(body: AccountCreateSchema):
            """
            Cria uma nova conta
            """
            return self.create_model(body)
       
        @self._app.patch('/account', tags=[self._tag],
                         responses={"201": AccountUpdateResponseSchema, "404": ErrorSchema})
        def update_account(query: GenericIdSchema, body: AccountUpdateSchema):
            """
            Atualiza uma conta de acordo com o ID informado
            """
            return self.update_model(query.id, body)
        
        @self._app.delete('/account', tags=[self._tag],
                          responses={"200": AccountDeleteResponseSchema, "404": ErrorSchema})
        def delete_account(query: GenericIdSchema):
            """
            Deleta uma conta de acordo com o ID informado
            """
            return self.delete_model(query.id)
