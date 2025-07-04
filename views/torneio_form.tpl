<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Criar Novo Torneio</title>
  <link href="/static/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt-5">
    <h2 class="mb-4">Criar Novo Torneio</h2>

    <form action="/torneios/create" method="post" class="card p-4 shadow-sm">
      <div class="mb-3">
        <label for="nome" class="form-label">Nome do Torneio</label>
        <input type="text" id="nome" name="nome" class="form-control" required>
      </div>

      <div class="mb-3">
        <label for="jogo" class="form-label">Jogo</label>
        <input type="text" id="jogo" name="jogo" class="form-control" required>
      </div>

      <div class="mb-3">
        <label class="form-label">Quantidade de Times</label><br>
        <div class="form-check form-check-inline">
          <input class="form-check-input" type="radio" name="tipo" id="tipo8" value="8" required>
          <label class="form-check-label" for="tipo8">8 Times</label>
        </div>
        <div class="form-check form-check-inline">
          <input class="form-check-input" type="radio" name="tipo" id="tipo16" value="16">
          <label class="form-check-label" for="tipo16">16 Times</label>
        </div>
      </div>

      <button type="submit" class="btn btn-success">Criar Torneio</button>
      <a href="/torneios" class="btn btn-secondary">Cancelar</a>
    </form>
  </div>
</body>
</html>
