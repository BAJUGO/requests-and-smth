from fastapi import APIRouter
from .currency_sb import router as currency_router

router = APIRouter(prefix="/sberbank", deprecated=True, tags=["SBERBANK"])

router.include_router(currency_router)

