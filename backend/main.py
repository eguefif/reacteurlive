from datetime import datetime

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import select

from db import SessionDep
from models.reactor import Reactor

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/plants")
async def plants(session: SessionDep) -> list[Reactor]:
    statement = select(Reactor)
    reactors = session.exec(statement).all()

    return list(reactors)
