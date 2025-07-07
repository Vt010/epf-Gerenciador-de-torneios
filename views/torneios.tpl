<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8>
    <title>Gaming Clash - Lista de Torneios</title>
    <link rel="stylesheet" href="/static/css/base.css">
    <link rel="stylesheet" href="/static/css/torneios.css">
</head>
<body class="torneios-page">

    <header class="top-bar">
        <a href="/dashboard" class="voltar"> Voltar ao Dashboard</a>
        <h1>Torneios Existentes</h1>
    </header>
    
    <main class="torneios-container">
        <h2 class="titulo-pagina">Torneios Ativos</h2>
        <p class="subtitulo-pagina"Participe dos melhores campeonatos!</p>

        <div class="cards-torneios">
            % for torneio in torneios:
                <div class="card-torneio">
                    <img class="logo-torneio" src="/static/img/{{torneio.logo}}.png" alt="{{torneio.jogo}} Logo">
                    <h3 class="Titulo-torneio">{{ torneio.nome }}</h3>
                    <p class="descricao-torneio">Máx Times: {{ torneio.max_times }}</p>
                    <a href="/times/inscrever/{{ torneio.id }}" class="btn-detalhes">Inscrever Time</a>

                </div>
            % end
        </div>

        <a href="/torneios/create" class="btn-criar">+ Criar Novo Torneio</a>
    </main>
    <ul>

</body>
</html>
