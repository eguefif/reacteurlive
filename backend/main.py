from fastapi import FastAPI

app = FastAPI()


def get_data():
    return []


@app.get("/data")
async def root() -> list[PlantState]:
    data = get_data()
    return data
