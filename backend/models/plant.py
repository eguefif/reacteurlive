from datetime import datetime

from sqlmodel import Field, SQLModel


class Plant(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    sector: str
    sub_sector: str
    commissioning_date: datetime
    powerMW: float
    min_powerMW: float
    gps: str
    city: str
    departement: int
    region: str
