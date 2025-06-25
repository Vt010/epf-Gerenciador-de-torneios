<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>

    % if error:
    <p style="color:red;">{{error}}</p>
    % end

    <form method="post" action="/login">
        <input type="email" name="email" placeholder="Email" required><br>
        <input type="password" name="password" placeholder="Senha" required><br>
        <button type="submit">Entrar</button>
    </form>

    <p>Não tem conta? <a href="/register">Cadastre-se</a></p>

</body>
</html>

