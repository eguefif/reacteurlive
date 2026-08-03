from datetime import datetime

from sqlmodel import Field, SQLModel


class Reactor(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    tranche: str
    fuel: str
    sector: str
    sub_sector: str
    commissioning_date: datetime
    powerMW: float
    min_powerMW: float
    gps: str
    city: str
    departement: int
    region: str

    status: str | None
    start_date: datetime | None
    end_date: datetime | None
    stop_type: str | None
    stop_reason: str | None
    information: str | None
    power_max: str | None
    power_available: str | None
