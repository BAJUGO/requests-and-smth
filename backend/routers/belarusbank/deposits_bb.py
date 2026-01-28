from fastapi import APIRouter
from requests import request


router = APIRouter(prefix="/belarusbank")


bb_link = "https://belarusbank.by/api/deposits_info"


@router.get("/all_deps")
async def get_all_deposits_bb():
    response = request("GET", url=bb_link)
    return response.json()