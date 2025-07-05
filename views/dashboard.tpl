<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Gaming Clash - Dashboard</title>
  <link rel="stylesheet" href="/static/css/base.css">
  <link rel="stylesheet" href="/static/css/dashboard.css">
</head>
<body class="dashboard">

  <div class="top-bar">
    Gaming Clash - Painel Principal
    <a href="/logout" class="logout-button">Sair</a>
  </div>

  <div class="dashboard-container">
    <img src="/static/img/GamingClash.png" alt="Logo" class="logo-dashboard">
    <h2 class="bemvindo">Bem-vindo, {{user.name}}!</h2>

    <div class="card-grid">


      <a href="/torneios" class="card">
        <h3>Torneios</h3>
        <p>Visualizar todos os campeonatos disponíveis.</p>
      </a>

      <a href="/perfil" class="card">
        <h3>Perfil</h3>
        <p>Visualize e edite suas informações.</p>
      </a>



      % if user.role == 'admin':
      <a href="/torneios/create" class="card admin">
        <h3>Criar Torneios</h3>
        <p>Adicionar novos campeonatos ao sistema.</p>
      </a>

      <a href="/torneios/edit" class="card admin">
        <h3>Editar Torneios</h3>
        <p>Modificar campeonatos existentes.</p>
      </a>

      % else:
      <div class="card disabled">
        <h3>Criar Torneios</h3>
        <p>(Somente para administradores)</p>
      </div>
      <div class="card disabled">
        <h3>Editar Torneios</h3>
        <p>(Somente para administradores)</p>
      </div>
      % end

      <a href="/sobre" class="card full-center">
        <h3>Sobre</h3>
        <p>Informações sobre o projeto Gaming Clash.</p>
      </a>

    </div>
  </div>

</body>
</html>
