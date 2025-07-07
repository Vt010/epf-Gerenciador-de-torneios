class Jogador:
    def __init__(self, nome):
        self.nome = nome

    def to_dict(self):
        return {'nome': self.nome}
    
    @classmethod
    def from_dict(cls, data):
        return cls(nome=data['nome'])
    
class Time:
    def __init__(self, id, nome, jogadores, usuario_id, torneio_id):
        self.id = id
        self.nome = nome
        self.jogadores = jogadores #lista
        self.usuario_id = usuario_id
        self.torneio_id = torneio_id

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'jogadores': [j.to_dict() for j in self.jogadores],
            'usuario_id': self.usuario_id,
            'torneio_id': self.torneio_id
        }
    
    @classmethod
    def from_dict(cls, data):
        jogadores = [Jogador.from_dict(j) for j in data['jogadores']]
        return cls(data['id'], data['nome'], jogadores, data['usuario_id'], data['torneio_id'])
    
        
        