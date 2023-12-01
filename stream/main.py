from fastapi import FastAPI
from contextlib import asynccontextmanager
from endpoint import router
from recognition import set_recognition
from video import set_video

@asynccontextmanager
async def lifespan(app: FastAPI):
    await set_recognition()
    await set_video()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)