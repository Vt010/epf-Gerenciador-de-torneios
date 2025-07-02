from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.torneio_service import TorneioService
import json

class TorneioController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.torneio_service = TorneioService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/torneios', method='GET', callback=self.listar)
        self.app.route('/torneios/create', method=['GET', 'POST'], callback=self.criar_torneio)
        self.app.route('/torneios/inscrever/<torneio_id:int>', method='POST', callback=self.inscrever_time)

    def listar_torneios(self):
        torneios = self.torneio_service.get_all()
        return self.render('torneios', torneios=torneios)

    def criar_torneio(self):
        if request.method == 'GET':
            return self.render('torneio_form')
        else:
            resultado = self.torneio_service.criar_torneio()
            if isinstance(resultado, str):
                return resultado
            return redirect('/torneios')

    def inscrever_time(self, torneio_id):
        time_nome = request.forms.get('time_nome')
        resultado = self.torneio_service.inscrever_time(torneio_id, time_nome)
        if isinstance(resultado, str):
            return resultado
        return redirect('/torneios')
    def listar(self):
        user = self.get_current_user()
        if not user:
            return self.redirect('/login')  # <- Isso é importante

        torneios = self.torneio_service.get_all()
        return self.render('torneios', torneios=torneios, user=user)



#inicializa as rotas
torneio_routes = Bottle()
torneio_controller = TorneioController(torneio_routes)
