from bottle import Bottle, request, template
from .base_controller import BaseController
from services.user_service import UserService
from models.user import UserModel

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.user_service = UserService()


    # Rotas User
    def setup_routes(self):
        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)
        self.app.route('/dashboard', method='GET', callback=self.dashboard)



    def list_users(self):
        users = self.user_service.get_all()
        return self.render('users', users=users)


    def add_user(self):
        if request.method == 'GET':
            return self.render('user_form', user=None, action="/users/add")
        else:
            # POST - salvar usuário
            self.user_service.save()
            self.redirect('/users')


    def edit_user(self, user_id):
        user = self.user_service.get_by_id(user_id)
        if not user:
            return "Usuário não encontrado"

        if request.method == 'GET':
            return self.render('user_form', user=user, action=f"/users/edit/{user_id}")
        else:
            # POST - salvar edição
            self.user_service.edit_user(user)
            self.redirect('/users')


    def delete_user(self, user_id):
        self.user_service.delete_user(user_id)
        self.redirect('/users')
        
    def dashboard(self):
        import json
        user_cookie = request.get_cookie('user')
        if not user_cookie:
            return self.redirect('/login')

        user_data = json.loads(user_cookie)
        return template('dashboard', user=user_data)


def user_dashboard():
    user_id = request.get_cookie('user_id')
    if not user_id:
        return "Acesso negado. Faça login."

    user_model = UserModel()
    user = user_model.get_by_id(int(user_id))

    if not user:
        return "Usuário não encontrado"

    return template('users', user=user)

user_routes = Bottle()
user_controller = UserController(user_routes)
