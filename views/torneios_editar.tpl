<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Editar Torneios</title>
    <link rel="stylesheet" href="/static/css/base.css">
    <link rel="stylesheet" href="/static/css/torneios.css">
</head>
<body class="torneios-page">

    <header class="top-bar">
        <a href="/dashboard" class="voltar">Voltar ao Dashboard</a>
        <h1>Editar Torneios</h1>
    </header>

    <main class="torneios-container">
        <h2 class="titulo-pagina">Gerenciar Torneios</h2>

        <div class="cards-torneios">
            % for torneio in torneios:
                <div class="card-torneio">
                    <h3 class="Titulo-torneio">{{ torneio.nome }}</h3>
                    <p class="descricao-torneio">Jogo: {{ torneio.jogo }}</p>
                    <p class="descricao-torneio">Máx. de Times: {{ torneio.max_times }}</p>

                    <a href="/torneios/{{ torneio.id }}/editar" class="btn-detalhes">✏️ Editar</a>

                    <form action="/torneios/{{ torneio.id }}/excluir" method="post" style="margin-top:10px;">
                        <button type="submit" class="btn-excluir" onclick="return confirm('Tem certeza que deseja excluir este torneio?')">
                            🗑️ Excluir
                        </button>
                    </form>
                </div>
            % end
        </div>

        <a href="/torneios/create" class="btn-criar">+ Criar Novo Torneio</a>
    </main>

</body>
</html>
