<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Editar Torneios</title>
    <link href="/static/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-5">

    <h2 class="mb-4">Torneios Cadastrados</h2>

    % if torneios:
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>Jogo</th>
                    <th>Qtd Times</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                % for torneio in torneios:
                    <tr>
                        <td>{{ torneio.nome }}</td>
                        <td>{{ torneio.jogo }}</td>
                        <td>{{ torneio.qtd_times }}</td>
                        <td>
                            <a href="/torneios/editar/{{ torneio.id }}" class="btn btn-sm btn-primary">Editar</a>
                        </td>
                    </tr>
                % end
            </tbody>
        </table>
    % else:
        <p>Nenhum torneio cadastrado.</p>
    % end

    <a href="/torneios" class="btn btn-secondary mt-3">Voltar</a>

</body>
</html>
