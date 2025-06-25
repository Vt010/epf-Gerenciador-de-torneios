from bottle import request, response, redirect 
#request para ler formulários, response para cookies, redirect para redirecionar páginas
from .base_controller import BaseController
from services.user_service import UserService
import json

class AuthController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes() #Cria as rotas de login/logout

    def setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/logout', method='GET', callback=self.logout)

    def login(self):
        if request.method == 'GET':
            #Se for GET, apenas renderiza o formulário de login
            return self.render('login', error=None)

        email = request.forms.get('email')  #Pega o e-mail digitado
        user = self.user_service.get_by_email(email)  #Busca o usuário com esse e-mail

        if user:
            #Se achou o usuário, converte os dados para dict e salva no cookie
            response.set_cookie('user', json.dumps(user.to_dict()), path='/')
            redirect('/users')  #Redireciona para a lista de usuários (ou página principal)
        else:
            return self.render('login', error="Usuário não encontrado")   

    def logout(self):
            response.delete_cookie('user')
            redirect('/login')


auth_routes = AuthController
