<!DOCTYPE html>
<html>
<head><title>Registro</title></head>
<body>
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
