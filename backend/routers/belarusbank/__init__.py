from fastapi import APIRouter
from .deposits_bb import router as deps_router
from .currency_bb import router as currency_router

router = APIRouter(prefix="/belarusbank", tags=["BELARUSBANK"])
router.include_router(deps_router)
router.include_router(currency_router)