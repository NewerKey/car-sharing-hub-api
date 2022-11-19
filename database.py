from sqlmodel import create_engine, Session
from schemas import SQLModel
from carsharing import app

engine = create_engine("sqlite:///carsharing.db",
                       connect_args={"check_same_thread": False},
                       echo=True)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
