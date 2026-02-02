from fastapi import APIRouter
import httpx
from transliterate import translit, detect_language


router = APIRouter(prefix="/currency", tags=["CURRENCY"])

bb_cur_link = "https://belarusbank.by/api/kursExchange"


@router.get("/all_everything", description="I don't know if anyone need this command")
async def get_all_everything_bb():
    r = httpx.get(bb_cur_link)
    return r.json()


@router.get("/all_exchanges_in_city/{city}")
async def get_all_exchanges_city(city: str):
    if not detect_language(city):
        city = translit(city, 'ru')
    r = httpx.get(bb_cur_link, params={"city": city})
    return r.json()


# The most useless function ever created by people
@router.get("/exchanges_in_city/{city}/{currencies}", description="In - bank buys, out - bank sells")
async def determined_exchanges_in_city(city: str, currency: str, in_or_out: str):
    if not detect_language(city):
        city = translit(city, 'ru')
    r = httpx.get(bb_cur_link, params={"city": city})
    final_banks = []
    for bank in r.json():
        final_bank = {
            "street": bank["street_type"] + bank["street"] + "" + bank["filials_text"],
            f"{currency.upper()}_{in_or_out}": f"{bank[f"{currency.upper()}_{in_or_out}"]}"
        }
        final_banks.append(final_bank)
    return final_banks



#TODO: Поработать с хаосом
@router.get("/chaos")
async def chaos():
    return httpx.get('https://belarusbank.by/open-banking/v1.0/banks/AKBBBY2X/services').json()