import os 
import json
from models.torneio import Torneio

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class TorneioModel:
    FILE_PATH = os.path.join(DATA_DIR, 'torneios.json')

    def __init__(self):
        self.torneios = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Torneio.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self.torneios], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.torneios

    def get_by_id(self, torneio_id):
        return next((t for t in self.torneios if t.id == torneio_id), None)

    def add(self, torneio: Torneio):
        self.torneios.append(torneio)
        self._save()

    def update(self, torneio: Torneio):
        for i, t in enumerate(self.torneios):
            if t.id == torneio.id:
                self.torneios[i] = torneio
                self._save()
                break

    def delete(self, torneio_id):
        self.torneios = [t for t in self.torneios if t.id != torneio_id]
        self._save()