from fastapi import status, APIRouter, Depends
from src.schemas.transaction import TransactionIn
from src.views.transaction import TransactionOut
from src.services.transaction import TransactionService
from src.security import login_required


router = APIRouter(prefix="/transactions", dependencies=[Depends(login_required)])

service = TransactionService()


@router.get("/{transaction_id}", response_model=TransactionOut)
async def read_transaction(transaction_id: int):
    return await service.read(transaction_id)


@router.get("/", response_model=list[TransactionOut])
async def read_all_transactions(limit: int, skip: int = 0):
    return await service.read_all(limit, skip)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionOut)
async def create_transaction(transaction: TransactionIn):
    return await service.create(transaction)
