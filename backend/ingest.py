import csv
from datetime import datetime

from sqlmodel import Session

from db import db_init, engine
from models.reactor import Reactor
from models.reactor_state import ReactorState

YEAR_FORMAT = "%Y-%m-%d"


def get_reactors() -> list[Reactor]:
    data = []
    with open("./plants.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=",")

        for entry in reader:
            plant = Reactor(
                name=entry["Centrale"],
                sector=entry["Sector"],
                sub_sector=entry["Sub-sector"],
                commissioning_date=datetime.strptime(
                    entry["Date de mise en service industrielle"], YEAR_FORMAT
                ),
                powerMW=float(entry["Puissance installée"]),
                min_powerMW=float(entry["Puissance minimum de conception"]),
                gps=entry["Point gps (wsg84)"],
                city=entry["Commune"],
                departement=int(entry["Code Insee département"]),
                region=entry["Région"],
            )
            data.append(plant)

    return data


def get_reactors_state() -> list[ReactorState]:
    data = []

    format = "%Y-%m-%d %H:%M:%S"
    with open("./plants_state.csv", "r", encoding="latin-1") as f:
        reader = csv.DictReader(f, delimiter=";")
        for entry in reader:
            data.append(
                ReactorState(
                    name=entry["Nom"],
                    status=entry["Status"],
                    stop_type=entry["Type"],
                    stop_reason=entry["Cause"],
                    start_date=datetime.strptime(entry["Date de début"], format),
                    end_date=datetime.strptime(entry["Date de fin"], format),
                    information=entry["Information complémentaire"],
                    power_max=entry["Puissance maximale (MW)"],
                    power_available=entry["Puissance disponible (MW)"],
                    published_at=datetime.strptime(
                        entry["Date de publication"], format
                    ),
                )
            )
    return data


def ingest():
    reactors = get_reactors()
    reactors_state = get_reactors_state()
    print("Ingesting ", len(reactors), "reactor entries")
    print("Ingesting ", len(reactors_state), "reactor state entries")
    with Session(engine) as session:
        session.bulk_save_objects(reactors)
        session.bulk_save_objects(reactors_state)
        session.commit()


if __name__ == "__main__":
    db_init()
    ingest()
