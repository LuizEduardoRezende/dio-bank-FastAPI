from fastapi import status, APIRouter, Depends, HTTPException
from src.schemas.account import AccountIn, AccountUpdateIn
from src.views.account import AccountOut
from src.services.account import AccountService
from src.security import login_required
from src.views.transaction import TransactionOut


router = APIRouter(prefix="/accounts", dependencies=[Depends(login_required)])

service = AccountService()


@router.get("/", response_model=list[AccountOut])
async def read_all_accounts(is_active: str, limit: int, skip: int = 0):
    published_bool = (
        is_active.lower() == "on" if isinstance(is_active, str) else is_active
    )
    return await service.read_all(published_bool, limit, skip)


@router.get("/{account_id}", response_model=AccountOut)
async def read_account(account_id: int):
    return await service.read(account_id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AccountOut)
async def create_account(account: AccountIn):
    return await service.create(account)


@router.patch(
    "/{account_id}", status_code=status.HTTP_200_OK, response_model=AccountOut
)
async def update_account(account_id: int, account: AccountUpdateIn):
    return await service.update(account_id, account)


@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_account(account_id: int):
    await service.delete(account_id)


@router.get("/{account_id}/transactions", response_model=list[TransactionOut])
async def read_all_account_transactions(account_id: int):
    return await service.read_all_transactions(account_id)
