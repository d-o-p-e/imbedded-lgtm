from fastapi import FastAPI
from contextlib import asynccontextmanager
from endpoint import router
from recognition import set_recognition

@asynccontextmanager
async def lifespan(app: FastAPI):
    await set_recognition()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)