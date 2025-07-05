from bottle import request, redirect
from .base_controller import BaseController
from services.torneio_service import TorneioService

class TorneioController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.torneio_service = TorneioService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/torneios', method='GET', callback=self.listar)
        self.app.route('/torneios/create', method=['GET', 'POST'], callback=self.criar)

    def listar(self):
        torneios = self.torneio_service.get_all()
        return self.render('torneios', torneios=torneios)

    def criar(self):
        user = self.get_current_user()
        if not user or getattr(user, 'role', 'comum') != 'admin':
            return self.redirect('/login')

        if request.method == 'GET':
            return self.render('torneio_form')

        nome = request.forms.get('nome')
        jogo = request.forms.get('jogo')
        max_times = request.forms.get('tipo')

        self.torneio_service.criar_torneio(nome, jogo, max_times)
        return redirect('/torneios')


