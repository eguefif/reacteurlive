from fastapi import FastAPI
from sqlmodel import select

from db import SessionDep
from models.plant import Plant

app = FastAPI()


@app.get("/plants")
async def plants(session: SessionDep) -> list[Plant]:
    statement = select(Plant)
    plants = session.exec(statement).all()

    return list(plants)
