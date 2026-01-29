from fastapi import APIRouter
from requests import request
import httpx


router = APIRouter(prefix="/belarusbank")


bb_link = "https://belarusbank.by/api/deposits_info"


@router.get("/all_deps")
async def get_all_deposits():
    response = request("GET", url=bb_link)
    return response.json()


@router.get("/dep_by_id/{dep_id}")
async def get_dep_by_id(dep_id: int):
    response = request("GET", url=bb_link)
    return response.json().get(str(dep_id))


@router.get("/dep_by_currency/{currency}")
async def get_dep_by_currency(currency: str):
    response = request("GET", url=f"{bb_link}?deposit_currency={currency}")
    return response.json()


@router.get("/all_deps_https")
async def get_all_deposits():
    response = httpx.get(bb_link)
    return response.json()

# TODO: Selenium, httpx