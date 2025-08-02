from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from src.database import database
from src.controllers import transaction, account, auth

from src.exceptions import (
    NotFoundAccountError,
    NotFoundTransactionError,
    InvalidAmountError,
    InsufficientBalanceError,
    InvalidTransactionTypeError,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


tags_metadata = [
    {
        "name": "auth",
        "description": "Operações relacionadas à autenticação de usuários, como login e geração de tokens.",
    },
    {
        "name": "accounts",
        "description": "Operações para gerenciar contas bancárias: criar, listar, atualizar, deletar e consultar saldo.",
    },
    {
        "name": "transactions",
        "description": "Operações para realizar transações financeiras, como depósitos e saques em contas bancárias.",
    },
]

app = FastAPI(
    lifespan=lifespan,
    title="DIO Bank API - FastAPI",
    version="1.0.2",
    tags_metadata=tags_metadata,
    description="""
DIO Bank API ajuda você a gerenciar suas contas bancárias e transações.
## Contas
Você será capaz de fazer:
* **Criar contas**.
* **Recuperar contas**.
* **Atualizar contas**.
* **Deletar contas**.
* **Listar transações de uma conta**.

## Transações
Você será capaz de fazer:
* **Saque**.
* **Depósito**.
""",
    redoc_url=None,  # disable ReDoc documentation
    # docs_url=None,  # disable Swagger UI documentation
    # openapi_url = None # disable OpenAPI documentation
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)


app.include_router(auth.router, tags=["auth"])
app.include_router(account.router, tags=["accounts"])
app.include_router(transaction.router, tags=["transactions"])


@app.get("/")
async def root():
    return {"message": "Welcome to DIO Bank API - FastAPI"}


@app.exception_handler(NotFoundAccountError)
async def not_found_account_exception_handler(
    request: Request, exc: NotFoundAccountError
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": exc.message}
    )


@app.exception_handler(NotFoundTransactionError)
async def not_found_transaction_exception_handler(
    request: Request, exc: NotFoundTransactionError
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": exc.message}
    )


@app.exception_handler(InvalidAmountError)
async def invalid_amount_exception_handler(request: Request, exc: InvalidAmountError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"detail": exc.message}
    )


@app.exception_handler(InsufficientBalanceError)
async def insufficient_balance_exception_handler(
    request: Request, exc: InsufficientBalanceError
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"detail": exc.message}
    )


@app.exception_handler(InvalidTransactionTypeError)
async def invalid_transaction_type_exception_handler(
    request: Request, exc: InvalidTransactionTypeError
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"detail": exc.message}
    )
