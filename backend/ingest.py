import csv
from datetime import datetime

from sqlmodel import Session, insert

from db import db_init, engine
from models.reactor import Reactor

YEAR_FORMAT = "%Y-%m-%d"


def get_state(states: list[dict], tranche: str) -> dict | None:
    for state in states:
        if "name" in state.keys() and state["name"] == tranche:
            state.pop("name")
            return state
    return None


def get_reactors(states: list[dict]) -> list[dict[str, str | float | int | datetime]]:
    data = []
    with open("./plants.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=",")

        for entry in reader:
            state = get_state(states, entry["Tranche"])
            reactor = {
                "name": entry["Centrale"],
                "tranche": entry["Tranche"],
                "sector": entry["Filière"],
                "sub_sector": entry["Sous-filière"],
                "commissioning_date": datetime.strptime(
                    entry["Date de mise en service industrielle"], YEAR_FORMAT
                ),
                "powerMW": float(entry["Puissance installée"]),
                "min_powerMW": float(entry["Puissance minimum de conception"]),
                "gps": entry["Point gps (wsg84)"],
                "city": entry["Commune"],
                "departement": int(entry["Code Insee département"]),
                "region": entry["Région"],
                "fuel": entry["Combustible"],
            }
            if state:
                reactor = reactor | state

            data.append(reactor)

    return data


def get_reactor_id(reactors: list[Reactor], name: str) -> Reactor | None:
    for reactor in reactors:
        if reactor.tranche == name:
            return reactor
    return None


def get_states() -> list[dict]:
    data = []

    format = "%Y-%m-%d %H:%M:%S"
    with open("./plants_state.csv", "r", encoding="latin-1") as f:
        reader = csv.DictReader(f, delimiter=";")
        for entry in reader:
            start_date = datetime.strptime(entry["Date de début"], format)
            end_date = datetime.strptime(entry["Date de fin"], format)
            date_now = datetime.now()
            if date_now < start_date or date_now > end_date:
                continue

            data.append(
                {
                    "name": entry["Nom"],
                    "status": entry["Status"],
                    "stop_type": entry["Type"],
                    "stop_reason": entry["Cause"],
                    "start_date": start_date,
                    "end_date": end_date,
                    "information": entry["Information complémentaire"],
                    "power_available": entry["Puissance disponible (MW)"],
                    "published_at": datetime.strptime(
                        entry["Date de publication"], format
                    ),
                }
            )
    return data


def ingest():
    states = get_states()
    reactors = get_reactors(states)
    print("Ingesting ", len(reactors), "reactor entries")
    with Session(engine) as session:
        session.exec(insert(Reactor), params=reactors)
        session.commit()


if __name__ == "__main__":
    db_init()
    ingest()
