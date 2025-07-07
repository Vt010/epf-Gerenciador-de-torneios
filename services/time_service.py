import os
import json
from models.time import Time

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'times.json')

class TimeService:
    def __init__(self):
        self.times = self._load()

    def _load(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return [Time.from_dict(item) for item in json.load(f)]

    def _save(self):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self.times], f, indent=4, ensure_ascii=False)

    def criar_time(self, nome, jogadores, usuario_id, torneio_id):
        novo_id = len(self.times) + 1
        time = Time(novo_id, nome, jogadores, usuario_id, torneio_id)
        self.times.append(time)
        self._save()
        return time

    def get_times_por_torneio(self, torneio_id):
        return [t for t in self.times if t.torneio_id == torneio_id]
