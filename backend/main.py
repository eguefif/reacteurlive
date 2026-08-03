from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import select

from db import SessionDep
from models.reactor import Plant

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/plants")
async def plants(session: SessionDep) -> list[Plant]:
    statement = select(Plant)
    plants = session.exec(statement).all()

    return list(plants)
