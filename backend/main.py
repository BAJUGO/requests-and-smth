from fastapi import FastAPI
from routers.belarusbank import router as bb_router

prefix_api = "/api/v0.1.0"

app = FastAPI()


app.include_router(bb_router, prefix=prefix_api)
