import bottle
from bottle import get, template
from controllers.user_controller import user_routes, user_dashboard
from controllers.auth_controller import AuthController, auth_routes
from controllers.dashboard_controller import DashboardController
from controllers.torneio_controller import TorneioController
from controllers.time_controller import TimeController

def init_controllers(app):
    # Subapp com rotas de /users
    app.mount('/users', user_routes)
    

    app.mount('/auth', auth_routes)

    # Classe AuthController cuida de /login, /logout e /register
    TorneioController(app)
    AuthController(app)
    DashboardController(app)
    TimeController(app)

    # Página protegida principal
    get('/user')(user_dashboard)
    
 #Página inicial
    @app.route('/')
    def home():
        return template('home')
