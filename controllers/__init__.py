from controllers.user_controller import user_routes
from controllers.auth_controller import AuthController

def init_controllers(app):
    #Inicializa o UserController (rotas de usuário)
    app.mount('/users', user_routes)

    #Inicializa o AuthController (rotas de login/logout)
    AuthController(app)
