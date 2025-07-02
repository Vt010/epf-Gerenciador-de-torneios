import bottle
from bottle import get, template
from controllers.user_controller import user_routes, user_dashboard
from controllers.auth_controller import AuthController

def init_controllers(app):
    # Subapp com rotas de /users
    app.mount('/users', user_routes)

    # Classe AuthController cuida de /login, /logout e /register
    AuthController(app)

    # Página protegida principal
    get('/user')(user_dashboard)
    
 # Página inicial
    @app.route('/')
    def home():
        return template('home')
