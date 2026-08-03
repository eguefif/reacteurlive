from datetime import datetime

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import select

from db import SessionDep
from models.reactor import Reactor
from models.reactor_state import ReactorState

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/plants")
async def plants(session: SessionDep) -> list[Reactor]:
    statement = select(Reactor)
    reactors = session.exec(statement).all()

    return list(reactors)


@app.get("/reactor/{reactor_id}")
async def reactor_state(session: SessionDep, reactor_id: int) -> ReactorState | None:
    statement = (
        select(ReactorState)
        .where(ReactorState.reactor_id == reactor_id)
        .where(ReactorState.start_date < datetime.now())
        .where(ReactorState.end_date > datetime.now())
    )
    reactor = session.exec(statement).first()

    return reactor
