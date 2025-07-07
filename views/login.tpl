<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Login</title>
  <link rel="stylesheet" href="/static/css/base.css">
  <link rel="stylesheet" href="/static/css/login.css">
</head>

<body class="login-page">

    % if error:
    <p style="color:red;">{{error}}</p>
    % end

    <div class="top-bar">
     <a href="/" class="home-button"> HOME </a>
     <img src="/static/img/Icone-esquerdo1.png" alt="Ícone Esquerda" class="top-icon">
     Gaming Clash! Um lugar onde você e seus amigos batalham pela glória da vitória! 
     <img src="/static/img/icone-direito1.png" alt="Ícone Direito" class="top-icon">

    </div>

    <div class="login-box">
        <img src="/static/img/GamingClash.png" alt="Logo do Projeto" class="logo">
        <p class="slogan">DE JOGADORES, PARA CAMPEÕES!</p>

        <form method="post" action="/login">
            <input type="email" name="email" placeholder="Email" required><br>
            <input type="password" name="password" placeholder="Senha" required><br>
            <button type="submit">Login</button> 
        </form>

        <p class="register-link">Não tem conta? <a href="/register">Cadastre-se</a></p>

    </div>


</body>
</html>

