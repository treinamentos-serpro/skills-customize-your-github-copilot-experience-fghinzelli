# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar um catálogo de livros usando FastAPI. Você praticará métodos HTTP, validação de dados com modelos, códigos de status e operações CRUD.

## 📝 Tarefas

### 🛠️ Configurar a API e listar livros

#### Descrição

Prepare o ambiente, execute o servidor FastAPI e implemente as primeiras rotas para verificar a API e consultar o catálogo de livros.

#### Requisitos
O programa concluído deve:

- Instalar FastAPI e Uvicorn e iniciar o servidor com `uvicorn starter-code:app --reload`.
- Disponibilizar `GET /health`, retornando um indicador de que a API está funcionando.
- Disponibilizar `GET /books`, retornando a lista de livros, inclusive quando estiver vazia.
- Permitir explorar a documentação interativa gerada pelo FastAPI em `/docs`.

### 🛠️ Criar e consultar livros

#### Descrição

Defina o formato dos dados de um livro e implemente as rotas para cadastrar um livro e consultar um item específico pelo identificador.

#### Requisitos
O programa concluído deve:

- Definir um modelo de livro com identificador, título, autor e ano de publicação.
- Validar os dados recebidos usando modelos do Pydantic.
- Disponibilizar `POST /books`, salvar o novo livro e responder com o código HTTP `201`.
- Disponibilizar `GET /books/{book_id}` para retornar um livro existente.
- Responder com o código HTTP `404` quando o identificador não corresponder a um livro.

### 🛠️ Atualizar e remover livros

#### Descrição

Complete as operações CRUD permitindo editar os dados de um livro existente e removê-lo do catálogo.

#### Requisitos
O programa concluído deve:

- Disponibilizar `PUT /books/{book_id}` para atualizar título, autor e ano de publicação.
- Disponibilizar `DELETE /books/{book_id}` para remover um livro existente.
- Responder com `404` ao tentar atualizar ou remover um livro inexistente.
- Retornar uma resposta sem conteúdo com o código HTTP `204` após uma remoção bem-sucedida.
- Manter as alterações disponíveis durante a execução do servidor usando armazenamento em memória.
