from bottle import request, response, redirect, template 
#request para ler formulários, response para cookies, redirect para redirecionar páginas
from .base_controller import BaseController
from services.user_service import UserService
from models.user import UserModel, UsuarioComum
import json

class AuthController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes() #Cria as rotas de login/logout

    def setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/logout', method='GET', callback=self.logout)
        self.app.route('/register', method=['GET', 'POST'], callback=self.register)

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

    def login_get():
        return template('login')

    def login_post():
        form = request.forms
        email = form.get('email')
        password = form.get('password')

        user_model = UserModel()
        user = user_model.get_by_email(email)

        if not user or not user.check_password(password):
            return "Email ou senha inválidos"

        # Autenticado → setar cookie simples com ID
        response.set_cookie('user_id', str(user.id))
        return redirect('/user')

    def register(self):
        if request.method == 'GET':
            return template('register', error=None)

        form = request.forms
        name = form.get('name')
        email = form.get('email')
        password = form.get('password')
        confirm_password = form.get('confirm_password')

        if password != confirm_password:
            return self.render('register', error="Senhas não coincidem")

        user_model = UserModel()

        if user_model.get_by_email(email):
            return self.render('register', error="Email já cadastrado")

        new_id = max([u.id for u in user_model.get_all()], default=0) + 1
        user = UsuarioComum(id=new_id, name=name, email=email, birthdate="")
        user.set_password(password)
        user_model.add_user(user)

        return redirect('/login')



auth_routes = AuthController
