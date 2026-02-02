from fastapi import APIRouter
import httpx

router = APIRouter(prefix="/currency", tags=["CURRENCY"])

sb_cur_link = "https://developer.sber-bank.by/api/rates/v1/currencyExchange"


@router.get("/all_exchanges/{exchangeType}",
            description="I think that sberbank has bad endpoints, or somethings happened with their DNS (or with mine)")
async def all_exchanges(exchangeType: str):
    r = httpx.get(sb_cur_link, params={"exchangeType": exchangeType})
    return r.json()