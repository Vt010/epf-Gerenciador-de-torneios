from bottle import request, redirect
from .base_controller import BaseController
from services.time_service import TimeService
from models.time import Jogador

class TimeController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.time_service = TimeService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/times/inscrever/<torneio_id:int>', method='GET', callback=self.exibir_formulario)
        self.app.route('/times/inscrever', method='POST', callback=self.inscrever_time)

    def exibir_formulario(self, torneio_id):
        user = self.get_current_user()
        if not user or user.role != 'comum':
            return redirect('/login')
        return self.render('time_form', torneio_id=torneio_id)

    def inscrever_time(self):
        user = self.get_current_user()
        if not user or user.role != 'comum':
            return redirect('/login')

        nome = request.forms.get('nome')
        torneio_id = int(request.forms.get('torneio_id'))
        jogadores = []

        for i in range(1, 7):
            nome_jogador = request.forms.get(f'jogador_{i}')
            if nome_jogador:
                jogadores.append(Jogador(nome_jogador))

        if len(jogadores) < 5:
            return "Erro: pelo menos 5 jogadores são obrigatórios."

        self.time_service.criar_time(nome, jogadores, user.id, torneio_id)
        return redirect(f'/torneios')
