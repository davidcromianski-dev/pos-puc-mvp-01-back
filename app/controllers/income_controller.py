from .abstract_controller import AbstractController
from ..services.income_service import IncomeService
from flask_openapi3.models.tag import Tag
from ..schemas.error import ErrorSchema
from ..schemas.generic import GenericIdSchema
from ..schemas.income_schema import IncomeResponseSchema, IncomesResponseSchema, IncomeUpdateResponseSchema, IncomeDeleteResponseSchema, IncomeCreateSchema, IncomeUpdateSchema

class IncomeController(AbstractController):
    def __init__(self, app):
        super().__init__(
            app,
            service=IncomeService,
            domain='incomes',
            name=__name__,
        )
        self._tag = Tag(name="Receitas", description="Adição, visualização e remoção de receitas à base")
        
    def register(self):
        @self._app.get('/incomes', tags=[self._tag],
                       responses={"200": IncomesResponseSchema, "404": ErrorSchema})
        @self._app.get('/incomes/', tags=[self._tag],
                       responses={"200": IncomesResponseSchema, "404": ErrorSchema})
        def list_incomes():
            """
            Lista todas as receitas do sistema
            """
            return self.list_models()
        
        @self._app.get('/income', tags=[self._tag],
                       responses={"200": IncomeResponseSchema, "404": ErrorSchema})
        def get_income(query: GenericIdSchema):
            """
            Lista uma receita de acordo com o ID informado
            """
            return self.get_model(query.id)
        
        @self._app.post('/income', tags=[self._tag],
                        responses={"201": IncomeResponseSchema, "409": ErrorSchema, "400": ErrorSchema})
        def create_income(body: IncomeCreateSchema):
            """
            Cria uma nova receita
            """
            return self.create_model(body)
       
        @self._app.patch('/income', tags=[self._tag],
                         responses={"201": IncomeUpdateResponseSchema, "404": ErrorSchema})
        def update_income(query: GenericIdSchema, body: IncomeUpdateSchema):
            """
            Atualiza uma receita de acordo com o ID informado
            """
            return self.update_model(query.id, body)
        
        @self._app.delete('/income', tags=[self._tag],
                          responses={"200": IncomeDeleteResponseSchema, "404": ErrorSchema})
        def delete_income(query: GenericIdSchema):
            """
            Deleta uma receita de acordo com o ID informado
            """
            return self.delete_model(query.id)
