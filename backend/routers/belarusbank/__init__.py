from fastapi import APIRouter
from .deposits_bb import router as deps_router

router = APIRouter(prefix="/belarusbank", tags=["BELARUSBANK"])
router.include_router(deps_router)