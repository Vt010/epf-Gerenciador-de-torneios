<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Editar Torneios</title>
  <link rel="stylesheet" href="/static/css/base.css">
  <link rel="stylesheet" href="/static/css/torneios_editar.css">
</head>
<body class="torneios-page">

  <!-- Topo com botão de voltar -->
  <div class="top-bar">
    <a href="/dashboard" class="botao-voltar-estilizado">Voltar ao Dashboard</a>
    <h1 class="titulo-topo">Torneios Existentes</h1>
</div>

  <div class="torneios-container">
    
    <!-- Cards de torneios -->
    <div class="cards-torneios">
      % for torneio in torneios:
        <div class="card-torneio">
          <div class="titulo-torneio">{{ torneio.nome }}</div>
          <div class="descricao-torneio">
            <strong>Jogo:</strong> {{ torneio.jogo }}<br>
            <strong>Máx. de Times:</strong> {{ torneio.max_times }}
          </div>

          <a href="/torneios/{{ torneio.id }}/editar" class="btn-detalhes">✏️ Editar</a>

          <form action="/torneios/{{ torneio.id }}/excluir" method="post" style="margin-top: 10px;">
            <button type="submit" class="btn-excluir">🗑️ Excluir</button>
          </form>
        </div>
      % end
    </div>

    <!-- Botão de criar novo torneio -->
    <div style="margin-top: 40px;">
      <a href="/torneios/create" class="btn-criar">+ Criar Novo Torneio</a>
    </div>

  </div>

</body>
</html>
