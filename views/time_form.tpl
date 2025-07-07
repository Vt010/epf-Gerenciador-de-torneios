<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Inscrever Time - Gaming Clash</title>
    <link rel="stylesheet" href="/static/css/base.css">
    <link rel="stylesheet" href="/static/css/time_form.css">
</head>
<body class="torneios-page">

    <header class="top-bar">
        <a href="/torneios" class="voltar">Voltar para Torneio</a>
        <h1>Inscrição de Time</h1>
    </header>

    <main class="torneios-container">
        <h2 class="titulo-pagina">Formulário de Inscrição</h2>

        <form action="/times/inscrever" method="post" class="form-inscricao">
            <input type="hidden" name="torneio_id" value="{{torneio_id}}">

            <label for="nome">Nome do Time:</label>
            <input type="text" id="nome" name="nome" required>

            <label for="jogador_1">Nick do Jogador 1:</label>
            <input type="text" id="jogador_1" name="jogador_1" required>

            <label for="jogador_2">Nick do Jogador 2:</label>
            <input type="text" id="jogador_2" name="jogador_2" required>

            <label for="jogador_3">Nick do Jogador 3:</label>
            <input type="text" id="jogador_3" name="jogador_3" required>

            <label for="jogador_4">Nick do Jogador 4:</label>
            <input type="text" id="jogador_4" name="jogador_4" required>

            <label for="jogador_5">Nick do Jogador 5:</label>
            <input type="text" id="jogador_5" name="jogador_5" required>

            <label for="jogador_6">Nick do Jogador 6 "reserva" (opcional):</label>
            <input type="text" id="jogador_6" name="jogador_6">

            <button type="submit" class="btn-criar">Confirmar Inscrição</button>
        </form>
    </main>

</body>
</html>
