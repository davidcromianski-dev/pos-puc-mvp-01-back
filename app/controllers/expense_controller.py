from .abstract_controller import AbstractController
from ..services.expense_service import ExpenseService
from flask_openapi3.models.tag import Tag
from ..schemas.error import ErrorSchema
from ..schemas.generic import GenericIdSchema
from ..schemas.expense_schema import ExpensesResponseSchema, ExpenseResponseSchema, ExpenseCreateSchema, ExpenseUpdateSchema, ExpenseDeleteResponseSchema, ExpenseUpdateResponseSchema

class ExpenseController(AbstractController):
    def __init__(self, app):
        super().__init__(
            app,
            service=ExpenseService,
            domain='expenses',
            name=__name__,
        )
        self._tag = Tag(name="Despesas", description="Adição, visualização e remoção de despesas à base")
    
    def register(self):
        @self._app.get('/expenses', tags=[self._tag],
                       responses={"200": ExpensesResponseSchema, "404": ErrorSchema})
        @self._app.get('/expenses/', tags=[self._tag],
                       responses={"200": ExpensesResponseSchema, "404": ErrorSchema})
        def list_expenses():
            """
            Lista todas as despesas do sistema
            """
            return self.list_models()
        
        @self._app.get('/expense', tags=[self._tag],
                       responses={"200": ExpenseResponseSchema, "404": ErrorSchema})
        def get_expense(query: GenericIdSchema):
            """
            Lista uma despesa de acordo com o ID informado
            """
            return self.get_model(query.id)
        
        @self._app.post('/expense', tags=[self._tag],
                        responses={"201": ExpenseResponseSchema, "409": ErrorSchema, "400": ErrorSchema})
        def create_expense(body: ExpenseCreateSchema):
            """
            Cria uma nova despesa
            """
            return self.create_model(body)
       
        @self._app.patch('/expense', tags=[self._tag],
                         responses={"201": ExpenseUpdateResponseSchema, "404": ErrorSchema})
        def update_expense(query: GenericIdSchema, body: ExpenseUpdateSchema):
            """
            Atualiza uma despesa de acordo com o ID informado
            """
            return self.update_model(query.id, body)
        
        @self._app.delete('/expense', tags=[self._tag],
                          responses={"200": ExpenseDeleteResponseSchema, "404": ErrorSchema})
        def delete_expense(query: GenericIdSchema):
            """
            Deleta uma despesa de acordo com o ID informado
            """
            return self.delete_model(query.id)
