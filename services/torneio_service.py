import os
import json
from models.torneio import Torneio

DATA_PATH = './data/torneios.json'

class TorneioService:
    def __init__(self):
        if not os.path.exists(DATA_PATH):
            with open(DATA_PATH, 'w') as f:
                json.dump([], f)

    def salvar(self, torneios):
        with open(DATA_PATH, 'w') as f:
            json.dump([t.to_dict() for t in torneios], f)

    def get_all(self):
        with open(DATA_PATH, 'r') as f:
            data = json.load(f)
            return [Torneio.from_dict(d) for d in data]

    def criar_torneio(self, nome, jogo, qtd_times):
        torneios = self.get_all()
        novo_id = max([t.id for t in torneios], default=0) + 1
        novo = Torneio(novo_id, nome, jogo, int(qtd_times))
        torneios.append(novo)
        self.salvar(torneios)
        return novo
