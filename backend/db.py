from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///database.db")


def db_init():
    import models.plant_state

    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    db_init()
