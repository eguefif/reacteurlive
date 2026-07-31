import csv
from datetime import datetime
from typing import Any

from sqlmodel import Session

from db import db_init, engine
from models.plant import Plant

PLANT_STATE_URL = "https://www.edf.fr/doaat/export/light/csv"

FORMAT = "%Y-%m-%d %H:%M:%S"
YEAR_FORMAT = "%Y-%m-%d"

# expected_keys = [
#        "Status",
#        "Identifiant",
#        "Numéro de version",
#        "Nom",
#        "Filière",
#        "Date de début",
#        "Date de fin",
#        "Type",
#        "Cause",
#        "Information complémentaire",
#        "Puissance maximale (MW)",
#        "Puissance disponible (MW)",
#        "Date de publication",
#    ]

plant_expected_keys = [
    "Sector",
    "Date de mise en service",
    "Puissance installée",
    "Point gps (wsg84)",
    "Commune",
    "Département",
    "Région",
    "Sub-sector",
    "Centrale",
]


def check_keys(entry_keys: list[Any] | None, expected_keys: list[str]) -> bool:
    if entry_keys == None:
        return False
    for key in entry_keys:
        print(key)
        if key not in expected_keys:
            return False
    return True


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
                power=float(entry["Puissance installée"]),
                gps=entry["Point gps (wsg84)"],
                city=entry["Commune"],
                departement=int(entry["Code Insee département"]),
                region=entry["Région"],
            )
            data.append(plant)

    return data


# def get_data() -> list[PlantState]:
#     data = []
#     print("reader data")
#     with open("./data.csv", "r", newline="", encoding="latin-1") as f:
#         reader = csv.DictReader(f, delimiter=";")
#
#         for entry in reader:
#             if check_keys(list(entry.keys())) == False:
#                 continue
#             plant = PlantState(
#                 status=entry["Status"],
#                 name=entry["Nom"],
#                 sector=entry["Filière"],
#                 start_date=datetime.strptime(entry["Date de début"], format),
#                 end_date=datetime.strptime(entry["Date de fin"], format),
#                 stop_type=entry["Type"],
#                 stop_reason=entry["Cause"],
#                 information=entry["Information complémentaire"],
#                 power_max=entry["Puissance maximale (MW)"],
#                 power_available=entry["Puissance disponible (MW)"],
#                 published_at=datetime.strptime(entry["Date de publication"], format),
#             )
#             data.append(plant)
#
#     return data


def ingest():
    data = get_plant()
    print(len(data))
    with Session(engine) as session:
        session.bulk_save_objects(data)
        session.commit()


if __name__ == "__main__":
    db_init()
    ingest()
