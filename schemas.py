# import json

from sqlmodel import SQLModel, Field, Relationship


class TripInput(SQLModel):
    start: int
    end: int
    description: str


class TripOutput(TripInput):
    id: int


class Trip(TripInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    car_id: int = Field(foreign_key="car.id")
    car: "Car" = Relationship(back_populates="trips")


class CarInput(SQLModel):
    size: str
    fuel: str
    doors: int
    transmission: str

    class Config:
        schema_extra = {
            "example": {
                "size": "m",
                "doors": 5,
                "transmission": "manual",
                "fuel": "hybrid"
            }
        }


class Car(CarInput, table=True):
    id: int | None = Field(primary_key=True, default=None)
    trips: list[Trip] = Relationship(back_populates="car")


class CarOutput(CarInput):
    id: int
    trips: list[TripOutput] = []


# def load_db() -> list[CarOutput]:
#     """Load a list of Car objects from a JSON file"""
#     with open("cars.json") as f:
#         return [CarInput.parse_obj(obj) for obj in json.load(f)]
#
#
# def save_db(cars: list[CarInput]):
#     with open("cars.json", 'w') as f:
#         json.dump([car.dict() for car in cars], f, indent=4)
