from models.torneio import Torneio
from models.torneioModel import TorneioModel
import json
from bottle import request

class TorneioService:
    def __init__(self):
        self.model = TorneioModel()

    def get_all(self):
        return self.model.get_all()

    def get_by_id(self, torneioId):
        return self.model.get_by_id(torneioId)

    def criar_torneio(self):
        user_cookie = request.get_cookie('user')
        if not user_cookie:
            return "Não autorizado"

        user_data = json.loads(user_cookie)
        if user_data.get('role') != 'admin':
            return "Apenas administradores podem criar torneios"

        nome = request.forms.get('nome')
        jogo = request.forms.get('jogo')
        tipo = request.forms.get('tipo')  #"8" ou "16"

        maxTimes = 8 if tipo == "8" else 16
        novoId = len(self.model.get_all()) + 1

        torneio = Torneio(
            id=novoId,
            nome=nome,
            jogo=jogo,
            maxTimes=maxTimes
        )

        self.model.add(torneio)

    def inscreverTime(self, torneioId, timeNome):
        torneio = self.model.get_by_id(torneioId)
        if not torneio:
            return "Torneio não encontrado"

        if torneio.status != 'ativo':
            return "Torneio encerrado"

        if len(torneio.timesInscritos) >= torneio.maxTimes:
            return "Torneio cheio"

        if timeNome in torneio.timesInscritos:
            return "Time já inscrito"

        torneio.timesInscritos.append(timeNome)
        self.model.update(torneio)
