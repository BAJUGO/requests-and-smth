from fastapi import FastAPI
from routers.belarusbank import router as bb_router
from routers.sberbank import router as sb_router

prefix_api = "/api/v0.1.0"

app = FastAPI()


app.include_router(bb_router, prefix=prefix_api)
app.include_router(sb_router, prefix=prefix_api)
