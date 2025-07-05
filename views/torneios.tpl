<!DOCTYPE html>
<html>
<head>
    <title>Lista de Torneios</title>
</head>
<body>
    <h1>Torneios</h1>
    <ul>
        % for torneio in torneios:
            <li>{{ torneio.nome }} - Máx Times: {{ torneio.max_times }}</li>
        % end
    </ul>
    <a href="/torneios/create">Criar novo torneio</a>
</body>
</html>
