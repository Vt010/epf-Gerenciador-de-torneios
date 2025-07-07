# Projeto Template: POO com Python + Bottle + JSON

Este é um projeto de template educacional voltado para o ensino de **Programação Orientada a Objetos (POO)** do Prof. Lucas Boaventura, Universidade de Brasília (UnB).

Utiliza o microframework **Bottle**. Ideal para uso em disciplinas introdutórias de Engenharia de Software ou Ciência da Computação.

📘 Projeto: Gerenciador de Torneios Gaming Clash
Sistema web para gerenciamento de torneios de e-sports com funcionalidades voltadas para administradores e usuários comuns. Desenvolvido em Python com o microframework Bottle e arquitetura orientada a objetos.

## 🚀 Funcionalidades

>👤 Autenticação
    ->Registro e login de usuários com diferenciação de tipo:

        .Administrador: acesso total

        .Comum: apenas inscrição em torneios

    ->Sessão via cookie simples (sem criptografia)

🏆 Torneios

>Administrador:

    .Criar torneios (nome, jogo, quantidade máxima de times)

    .   Editar torneios:

        Alterar quantidade máxima de times

        Excluir torneio

>Usuário Comum

    .Visualizar torneios ativos

    .Inscrever time em torneio

>🧑‍🤝‍🧑 Times
    .Cada usuário comum pode cadastrar o time no torneio

    Cada time contém:

        Nome do time

        De 5 a 6 jogadores (nicknames)
---

## 🗂 Estrutura de Pastas

```bash
poo-python-bottle-template/
├── app.py # Ponto de entrada do sistema
├── config.py # Configurações e caminhos do projeto
├── main.py # Inicialização da aplicação
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
├── controllers/ # Controladores e rotas
├── models/ # Definição das entidades (ex: User)
├── services/ # Lógica de persistência (JSON)
├── views/ # Arquivos HTML (Bottle Templating)
├── static/ # CSS, JS e imagens
├── data/ # Arquivos JSON de dados
└── .vscode/ # Configurações opcionais do VS Code
```


---
## 📘 Diagrama de Classes

!Diagrama (static/img/diagrama.png)
+-------------------+
|     UserModel     |
+-------------------+
| - id              |
| - nome            |
| - email           |
| - senha           |
| - role            |
+-------------------+

           ▲
           |
+---------------------+
|  Administrador      |   
+---------------------+
| (herda de UserModel)|
+---------------------+
+---------------------+
|  UsuarioComum       |
+---------------------+
| (herda de UserModel)|
+---------------------+

+-------------------+
|     Torneio       |
+-------------------+
| - id              |
| - nome            |
| - jogo            |
| - status          |
| - max_times       |
+-------------------+

+-------------------+
|      Time         |
+-------------------+
| - id              |
| - nome            |
| - jogadores[]     |
| - usuario_id      |
| - torneio_id      |
+-------------------+

+-------------------+
|     Jogador       |
+-------------------+
| - nome            |
+-------------------+


---

## ▶️ Como Executar

1. Crie o ambiente virtual na pasta fora do seu projeto:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

2. Entre dentro do seu projeto criado a partir do template e instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a aplicação:
```bash
python main.py
```

4. Accese sua aplicação no navegador em: [http://localhost:8080](http://localhost:8080)


## ✅ Tecnologias Utilizadas
    .Python 3.12

    .Bottle

    .HTML5 + CSS3

    .Armazenamento em arquivos JSON
