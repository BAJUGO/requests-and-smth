from fastapi import APIRouter
from requests import request
import httpx


router = APIRouter(prefix="/deps", tags=["DEPS"])


bb_dep_link = "https://belarusbank.by/api/deposits_info"


@router.get("/all_deps")
async def get_all_deps():
    r = httpx.get(bb_dep_link)
    return r.json()


@router.get("/dep_by_id/{dep_id}")
async def get_dep_by_id(dep_id: int):
    r = httpx.get(bb_dep_link)
    return r.json().get(str(dep_id))


@router.get("/dep_by_currency/{currency}")
async def get_dep_by_currency(currency: str):
    r = httpx.get(url=bb_dep_link, params={"deposit_currency": currency})
    print(r.headers.get("content-type"))
    return r.json()


@router.get("/all_deps_in_short")
async def get_all_deps_in_short():
    r = httpx.get(url=bb_dep_link)
    r_jsoned = r.json()
    deps = []
    for dep in r_jsoned.values():
        dep_shorted = {"dep_id": dep["vklad_id"],
                       "dep_cur": dep["vklad_val"],
                       "dep_period": dep["vklad_srok_text"],
                       "dep_percent": dep["vklad_procent"],
                       "dep_min_sum": dep["vklad_minimal"]}
        deps.append(dep_shorted)
    return deps



# TODO: Selenium, httpx