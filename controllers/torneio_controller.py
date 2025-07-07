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
        self.app.route('/torneios/editar', method='GET', callback=self.listar_para_edicao)
        self.app.route('/torneios/<id:int>/editar', method='GET', callback=self.editar_form)
        self.app.route('/torneios/<id:int>/editar', method='POST', callback=self.processar_edicao)
        self.app.route('/torneios/<id:int>/excluir', method='POST', callback=self.excluir)

    def listar(self):
        torneios = self.torneio_service.get_all()
        
         # Dicionário de logos por nome do jogo
        logos = {
                "league of legends": "lol",
                "cs2": "cs2",
                "counter-strike 2": "cs2",
                "valorant": "valorant",
}

    # Cria um campo adicional em cada torneio com o nome da imagem
        for t in torneios:
            nome_jogo = t.jogo.strip().lower()
            t.logo = logos.get(nome_jogo, "default")  # fallback para 'default.png'
        
        return self.render('torneios', torneios=torneios)


    def criar(self):
        user = self.get_current_user()
        if not user or getattr(user, 'role', 'comum') != 'admin':
            return self.redirect('/login')

        if request.method == 'GET':
            jogos_disponiveis = [
                {"nome": "League of Legends", "logo": "lol.png"},
                {"nome": "CS2", "logo": "cs2.png"},
                {"nome": "Valorant", "logo": "valorant.png"},
            # É só adicionar mais jogos aqui 
            ]
            return self.render('torneio_form', torneio=None, jogos=jogos_disponiveis)
        nome = request.forms.get('nome')
        jogo = request.forms.get('jogo')
        max_times = request.forms.get('max_times')

        self.torneio_service.criar_torneio(nome, jogo, max_times)
        return redirect('/torneios')

    def listar_para_edicao(self):
        user = self.get_current_user()
        if not user or user.role != 'admin':
            return redirect ('/login')
        
        torneios = self.torneio_service.get_all()
        return self.render('torneios_editar', torneios=torneios)
    
    def editar_form(self, id):
        user = self.get_current_user()
        if not user or user.role != 'admin':
            return redirect('/login')

        torneio = self.torneio_service.get_by_id(id)
        logos = {
            "league of legends": "lol",
            "cs2": "cs2",
            "counter-strike 2": "cs2",
            "valorant": "valorant",
        }

        nome_jogo = torneio.jogo.strip().lower()
        torneio.logo = logos.get(nome_jogo, "default")

        jogos_disponiveis = [
            {"nome": "League of Legends", "logo": "lol.png"},
            {"nome": "CS2", "logo": "cs2.png"},
            {"nome": "Valorant", "logo": "valorant.png"},
        ]
        return self.render('torneio_form', torneio=torneio, jogos=jogos_disponiveis)

    
    def processar_edicao(self, id):
        user = self.get_current_user()
        if not user or user.role != 'admin':
            return redirect('/login')

        nome = request.forms.get('nome')
        jogo = request.forms.get('jogo')
        status = request.forms.get('status')
        max_times = int(request.forms.get('max_times'))

        self.torneio_service.atualizar_torneio(id, nome, jogo, status, max_times)
        return redirect('/torneios/editar')
    def excluir(self, id):
        user = self.get_current_user()
        if not user or user.role != 'admin':
            return redirect('/login')

        self.torneio_service.remover_torneio(id)
        return redirect('/torneios/editar')