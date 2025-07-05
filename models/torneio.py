class Torneio:
    def __init__(self, id, nome, jogo, max_times, times=None):
        self.id = id
        self.nome = nome
        self.jogo = jogo
        self.max_times = max_times  # 8 ou 16
        self.times = times if times else []

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'jogo': self.jogo,
            'max_times': self.max_times,
            'times': self.times
        }

    @staticmethod
    def from_dict(data):
        return Torneio(
            id=data['id'],
            nome=data['nome'],
            jogo=data['jogo'],
            max_times=data['max_times'],
            times=data.get('times', [])
        )
