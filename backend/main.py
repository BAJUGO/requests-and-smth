from fastapi import FastAPI
from routers.belarusbank.deposits_bb import router as bb_router


app = FastAPI(prefix="/api/v0.1.0")


app.include_router(bb_router)