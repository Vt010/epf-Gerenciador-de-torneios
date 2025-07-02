<h2 class="mt-4 mb-3">Torneios Disponíveis</h2>

<table class="table table-striped">
  <thead class="table-dark">
    <tr>
      <th>Nome</th>
      <th>Jogo</th>
      <th>Status</th>
      <th>Times inscritos</th>
      <th>Ações</th>
    </tr>
  </thead>
  <tbody>
    % for t in torneios:
      <tr>
        <td>{{ t.nome }}</td>
        <td>{{ t.jogo }}</td>
        <td>
          % if t.status == 'ativo':
            <span class="badge bg-success">Ativo</span>
          % else:
            <span class="badge bg-secondary">Encerrado</span>
          % end
        </td>
        <td>{{ len(t.times_inscritos) }}/{{ t.max_times }}</td>
        <td>
          % if t.status == 'ativo' and len(t.times_inscritos) < t.max_times:
            <form action="/torneios/inscrever/{{ t.id }}" method="post" class="d-flex">
              <input type="text" name="time_nome" placeholder="Nome do time" class="form-control form-control-sm me-2" required>
              <button type="submit" class="btn btn-primary btn-sm">Inscrever</button>
            </form>
          % else:
            <span class="text-muted">Inscrição indisponível</span>
          % end
        </td>
      </tr>
    % end
  </tbody>
</table>