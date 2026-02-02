from fastapi import APIRouter
import httpx


router = APIRouter(prefix="/currency", tags=["CURRENCY"])

bb_cur_link = "https://belarusbank.by/api/kursExchange"


@router.get("/all_everything", description="I don't know if anyone need this command")
async def get_all_everything_bb():
    r = httpx.get(bb_cur_link)
    return r.json()


