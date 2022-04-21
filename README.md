<h1 align="center">Resource Manager API</h1>


<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-v.3.8.x-346c94">
  <img alt="Flask" src="https://img.shields.io/badge/flask-v.2.1.x-040404">
</p>


## :hammer_and_wrench: Tecnologias
- [Python](https://www.python.org/)
- [Flask](https://palletsprojects.com/p/flask/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)


## :computer: Sobre o projeto
O Resource Manager API é um gerenciador de recursos desenvolvido com a linguagem de programação Python, o micro-framework Flask e o banco de dados PostgreSQL.


## :construction: Estrutura
```bash
.
├── Dockerfile
├── LICENSE
├── README.md
├── api
│   ├── __init__.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── admin_controllers.py
│   │   └── user_controllers.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── allocations.py
│   │   ├── resources.py
│   │   └── users.py
│   └── routes
│       ├── __init__.py
│       ├── admin_routes.py
│       └── user_routes.py
├── docker-compose.yml
├── documentation
│   └── endpoints.json
├── requirements.txt
└── server.py
```


## :zap: Funcionalidades

#### Administrador:
- Criar recursos;
- Listar todos os recursos no banco de dados;
- Atualizar disponibilidade dos recursos ("disponível" ou "indisponível");
- Deletar recursos;
- Deletar usuários.

#### Usuário:
- Criar um novo usuário;
- Ler dados de um usuário;
- Atualizar nome do usuário;
- Deletar um usuário;
- Listar todos os recursos "disponíveis" no banco de dados;
- Realizar alocação de um recurso;
- Realizar a devolução de um recurso.


## :page_facing_up: Documentação
Para verficar os endpoints da API acesse [aqui](https://lfnd0.github.io/resource-manager-challenge-docs/). Já para testar as rotas, importe no [Insomnia](https://insomnia.rest/) o arquivo localizado em [documentation](documentation/endpoints.json).


## :rocket: Como executar
Para executar esta API é necessário ter o Docker e o Docker Compose instalados.

1. Clonar o repositório do projeto
   ```bash
   git clone git@github.com:lfnd0/resource-manager-api.git
   ```
2. Executar dentro da raiz do projeto o comando:
   ```bash
   docker-compose up
   ```
3. Acessar o interpretador Python do container `api`:
   ```bash
   docker-compose exec api python3
   ```
4. Executar os dois comandos a seguir, um de cada vez, dentro do interpretador Python do container `api`:
   ```bash
   from api import database
   database.create_all()
   ```
5. Para testar as rotas da API, recomenda-se importar o arquivo localizado em [documentation](documentation/endpoints.json) no Insomnia.


## :link: Rotas

#### Administrador:
- **[GET]** create_admin: `/api/admin`
- **[POST]** create_resource: `/api/admin/resources`
- **[GET]** read_resources: `/api/admin/resources`
- **[PUT]** update_resource: `/api/admin/resources/{id}`
- **[DELETE]** delete_resource: `/api/admin/resources/{id}`
- **[DELETE]** delete_user_by_admin: `/api/admin/users/{id}`

#### Usuário:
- **[POST]** create_user: `/api/users`
- **[GET]** read_user: `/api/users/{id}`
- **[PUT]** update_user: `/api/users/{id}`
- **[DELETE]** delete_user: `/api/users/{id}`
- **[GET]** read_resources_available: `/api/users/resources`
- **[POST]** create_allocation: `/api/users/allocations`
- **[PUT]** update_allocation `/api/users/allocations/{id}`


## :mortar_board: Autor
[Luiz Fernando](https://lfnd0.github.io/)


## :page_facing_up: Licença
Este projeto está sob a [licença MIT](LICENSE).
