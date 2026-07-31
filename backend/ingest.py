import csv
from datetime import datetime

from sqlmodel import Session

from db import db_init, engine
from models.plant import Plant

YEAR_FORMAT = "%Y-%m-%d"


def get_plant() -> list[Plant]:
    data = []
    with open("./plants.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=",")

        for entry in reader:
            plant = Plant(
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


def ingest():
    data = get_plant()
    print(len(data))
    with Session(engine) as session:
        session.bulk_save_objects(data)
        session.commit()


if __name__ == "__main__":
    db_init()
    ingest()
