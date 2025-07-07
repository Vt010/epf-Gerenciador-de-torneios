<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Criar Novo Torneio</title>
  <link rel="stylesheet" href="/static/css/base.css">
  <link rel="stylesheet" href="/static/css/torneio_form.css">
  <link href="/static/bootstrap.min.css" rel="stylesheet"> <!-- Só se necessário -->
</head>
<body>
  <div class="torneio-container">
    <h1>CRIAR NOVO TORNEIO</h1>

  <form action="{{ '/torneios/' + str(torneio.id) + '/editar' if torneio else '/torneios/create' }}" method="post">
      <div class="form-topo">
  <div class="form-campos">
    <div class="input-group">
      <label for="nome">Nome do torneio:</label>
      <input type="text" id="nome" name="nome" required>
    </div>

    <div class="input-group">
      <label for="jogo">Jogo:</label>
      <select id="jogo" name="jogo" onchange="atualizarLogo()" required>
        <option value="" disabled selected>Selecione um jogo</option>
        % for jogo in jogos:
          <option value="{{jogo['nome']}}" data-logo="/static/img/{{jogo['logo']}}">{{jogo['nome']}}</option>
        % end
      </select>
    </div>
  </div>

  <div class="form-logo">
    <img id="logo-preview" src="" alt="Logo do jogo" style="display:none;">
  </div>
</div>


      <div class="selecao-times">
  <h2>Quantidade de Times</h2>

  <div class="radio-options-container">
    <div class="radio-option">
      <img src="/static/img/chave_16.png" alt="16 Times">
      <label>
        <input type="radio" name="max_times" value="16" required> 16 Times (Oitavas)
      </label>
    </div>

    <div class="radio-option">
      <img src="/static/img/chave_8.png" alt="8 Times">
      <label>
        <input type="radio" name="max_times" value="8" required> 8 Times (Quartas)
      </label>
    </div>
  </div>
</div>

      <div class="botoes-final">
        <button type="submit" class="btn-criar">CRIAR TORNEIO</button>
        <a href="/torneios" class="cancelar-link">Cancelar</a>
      </div>

    </form>
  </div>

  <script>
    function atualizarLogo() {
      const select = document.getElementById("jogo");
      const logo = document.getElementById("logo-preview");
      const selectedOption = select.options[select.selectedIndex];
      const logoUrl = selectedOption.getAttribute("data-logo");

      if (logoUrl) {
        logo.src = logoUrl;
        logo.style.display = "block";
      } else {
        logo.style.display = "none";
      }
    }
  </script>
</body>
</html>
