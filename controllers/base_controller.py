from bottle import static_file, request 
import json

class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()


    def _setup_base_routes(self):
        """Configura rotas básicas comuns a todos os controllers"""
        self.app.route('/', method='GET', callback=self.home_redirect)
        self.app.route('/helper', method=['GET'], callback=self.helper)

        # Rota para arquivos estáticos (CSS, JS, imagens)
        self.app.route('/static/<filename:path>', callback=self.serve_static)


    def home_redirect(self):
        """Redireciona a rota raiz para /users"""
        return self.redirect('/users')


    def helper(self):
        return self.render('helper-final')


    def serve_static(self, filename):
        """Serve arquivos estáticos da pasta static/"""
        return static_file(filename, root='./static')


    def render(self, template, **context):
        """Método auxiliar para renderizar templates"""
        from bottle import template as render_template
        return render_template(template, **context)


    def redirect(self, path):
        """Método auxiliar para redirecionamento"""
        from bottle import redirect as bottle_redirect
        return bottle_redirect(path)

    def get_current_user(self):
        from models.user import UsuarioComum, Administrador

        user_json = request.get_cookie('user')
        if not user_json:
            return None

        user_dict = json.loads(user_json)
        role = user_dict.get('role')

        if role == 'admin':
            return Administrador.from_dict(user_dict)
        else:
            return UsuarioComum.from_dict(user_dict)