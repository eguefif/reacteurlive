from datetime import datetime

from sqlmodel import Field, SQLModel


class ReactorState(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    status: str
    start_date: datetime
    end_date: datetime
    stop_type: str
    stop_reason: str
    information: str
    power_max: str | None
    power_available: str | None
    published_at: datetime

    plant_id: int | None = Field(default=None, foreign_key="plant.id")
