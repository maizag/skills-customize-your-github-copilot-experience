# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Nesta atividade, você vai construir uma API REST usando FastAPI para criar, listar, atualizar e remover recursos. Ao final, você terá praticado rotas HTTP, validação com modelos Pydantic e respostas JSON.

## 📝 Tarefas

### 🛠️ Criar a Estrutura Base da API

#### Descrição
Crie uma aplicação FastAPI com uma rota inicial e uma estrutura simples para armazenar itens em memória.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI` e executar a aplicação com `uvicorn`
- Implementar uma rota `GET /` que retorne uma mensagem JSON de status
- Definir um modelo `Item` com `id`, `name`, `price` e `in_stock`
- Manter uma lista ou dicionário em memória para simular um banco de dados

### 🛠️ Implementar Endpoints CRUD

#### Descrição
Implemente endpoints REST para criar, listar, buscar, atualizar e remover itens.

#### Requisitos
O programa concluído deve:

- Implementar `POST /items` para criar um item com validação de dados
- Implementar `GET /items` e `GET /items/{item_id}` para listagem e busca por ID
- Implementar `PUT /items/{item_id}` e `DELETE /items/{item_id}` para atualização e remoção
- Retornar códigos HTTP adequados (por exemplo: `201`, `200`, `404`)
