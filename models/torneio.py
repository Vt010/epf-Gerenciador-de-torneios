import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Torneio:
    def __init__(self, id, nome, jogo, maxTimes, status='ativo', timesInscritos=None):
        self.id = id
        self.nome = nome
        self.jogo = jogo
        self.maxTimes = maxTimes
        self.status = status
        self.timesInscritos = timesInscritos or []

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'jogo': self.jogo,
            'maxTimes': self.maxTimes,
            'status': self.status,
            'timesInscritos': self.timesInscritos
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            nome=data['nome'],
            jogo=data['jogo'],
            maxTimes=data['maxTimes'],
            status=data.get('status', 'ativo'),
            timesInscritos=data.get('timesInscritos', [])
        )