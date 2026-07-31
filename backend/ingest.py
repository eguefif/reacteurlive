import csv
from typing import Any

from sqlmodel import Session

from db import engine
from models.plant_state import PlantState


def check_keys(entry_keys: list[Any] | None) -> bool:
    if entry_keys == None:
        return False
    expected_keys = [
        "Status",
        "Identifiant",
        "Numéro de version",
        "Nom",
        "Filière",
        "Date de début",
        "Date de fin",
        "Type",
        "Cause",
        "Information complémentaire",
        "Puissance maximale (MW)",
        "Puissance disponible (MW)",
        "Date de publication",
    ]
    for key in entry_keys:
        if key not in expected_keys:
            return False
    return True


def get_data() -> list[PlantState]:
    # format = "%Y-%m-%d %H:%M:%S"
    data = []
    print("reader data")
    with open("./data.csv", "r", newline="", encoding="latin-1") as f:
        reader = csv.DictReader(f, delimiter=";")

        for entry in reader:
            if check_keys(list(entry.keys())) == False:
                continue
            plant = PlantState(
                status=entry["Status"],
                name=entry["Nom"],
                sector=entry["Filière"],
                # start_date=datetime.strptime(entry["Date de début"], format),
                # end_date=datetime.strptime(entry["Date de fin"], format),
                stop_type=entry["Type"],
                stop_reason=entry["Cause"],
                information=entry["Information complémentaire"],
                power_max=entry["Puissance maximale (MW)"],
                power_available=entry["Puissance disponible (MW)"],
                # published_at=datetime.strptime(entry["Date de publication"], format),
            )
            data.append(plant)

    return data


def ingest():
    data = get_data()
    with Session(engine) as session:
        session.bulk_save_objects(data)
        session.commit()


if __name__ == "__main__":
    ingest()
