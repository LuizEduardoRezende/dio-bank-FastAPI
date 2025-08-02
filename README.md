# 🏦 DIO Bank FastAPI

Uma API RESTful moderna e assíncrona para gerenciamento bancário, desenvolvida com FastAPI e SQLAlchemy. Este projeto faz parte da formação Python Backend da DIO (Digital Innovation One) e implementa um sistema bancário completo com operações de contas e transações.

## 🚀 Tecnologias Utilizadas

- **FastAPI** - Framework web moderno e de alta performance
- **SQLAlchemy** - ORM para Python
- **Alembic** - Gerenciamento de migrações de banco de dados
- **Pydantic** - Validação de dados
- **JWT** - Autenticação baseada em tokens
- **Uvicorn** - Servidor ASGI de alta performance
- **Python 3.13+** - Linguagem de programação

## 📋 Funcionalidades

### 🔐 Autenticação
- Sistema de login com JWT tokens
- Middleware de autenticação para rotas protegidas

### 💳 Gerenciamento de Contas
- ✅ Criar novas contas bancárias
- ✅ Listar todas as contas
- ✅ Consultar detalhes de uma conta específica
- ✅ Atualizar informações da conta
- ✅ Desativar contas
- ✅ Consultar saldo

### 💰 Transações Financeiras
- ✅ Realizar depósitos
- ✅ Realizar saques
- ✅ Histórico de transações
- ✅ Validação de saldo suficiente
- ✅ Controle de tipos de transação

## 🏗️ Estrutura do Projeto

```
dio-bank-fastapi/
├── src/
│   ├── controllers/          # Controladores da API
│   │   ├── account.py        # Endpoints de contas
│   │   ├── auth.py           # Endpoints de autenticação
│   │   └── transaction.py    # Endpoints de transações
│   ├── models/              # Modelos de banco de dados
│   │   ├── account.py       # Modelo de conta
│   │   └── transaction.py   # Modelo de transação
│   ├── schemas/             # Schemas Pydantic
│   ├── services/            # Lógica de negócio
│   ├── views/              # Modelos de resposta
│   ├── config.py           # Configurações da aplicação
│   ├── database.py         # Configuração do banco de dados
│   ├── exceptions.py       # Exceções customizadas
│   ├── security.py         # Utilitários de segurança
│   └── main.py            # Aplicação principal
├── migrations/            # Migrações Alembic
├── alembic.ini            # Configuração do Alembic
├── pyproject.toml         # Dependências e configurações
└── README.md              # Este arquivo
```

## ⚙️ Configuração e Instalação

### Pré-requisitos
- Python 3.13 ou superior
- Poetry (recomendado) ou pip

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd dio-bank-fastapi
```

### 2. Instale as dependências
```bash
# Com Poetry (recomendado)
poetry install

# Ou com pip
pip install -r requirements.txt
```

### 3. Configure o banco de dados
```bash
# Execute as migrações
alembic upgrade head
```

### 4. Execute a aplicação
```bash
# Com Poetry
poetry run uvicorn src.main:app --reload

# Ou diretamente
uvicorn src.main:app --reload
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

Após executar a aplicação, acesse:

- **Swagger UI**: `http://localhost:8000/docs`


## 🎓 Sobre o Projeto

Este projeto foi desenvolvido como parte da **Formação Python Backend** da [Digital Innovation One (DIO)](https://dio.me), focando no aprendizado de:

- Desenvolvimento de APIs REST com FastAPI
- Programação assíncrona em Python
- Autenticação e autorização
- Modelagem de banco de dados
- Testes automatizados
- Boas práticas de desenvolvimento

