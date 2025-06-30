<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Registro</title>
  <link rel="stylesheet" href="/static/css/base.css">
  <link rel="stylesheet" href="/static/css/register.css">
</head>

<body>
<div class="top-bar">
    <img src="/static/img/Icone-esquerdo1.png" alt="Ícone Esquerda" class="top-icon">
    Gaming Clash! Um lugar onde você e seus amigos batalham pela glória da vitória! 
    <img src="/static/img/icone-direito1.png" alt="Ícone Direito" class="top-icon">
</div>
  <h2>Cadastro</h2>
  % if error:
    <p style="color: red;">{{error}}</p>
  % end
  <form method="post">
    <input name="name" placeholder="Nome" required>
    <input name="email" type="email" placeholder="Email" required>
    <input name="password" type="password" placeholder="Senha" required>
    <input name="confirm_password" type="password" placeholder="Confirmar Senha" required>
    <button type="submit">Registrar</button>
  </form>
</body>
</html>
