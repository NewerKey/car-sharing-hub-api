import json

from pydantic import BaseModel


class Car(BaseModel):
    id: int
    size: str
    fuel: str
    doors: int
    transmission: str


def load_db() -> list[Car]:
    """Load a list of Car objects from a JSON file"""
    with open("cars.json") as f:
        return [Car.parse_obj(obj) for obj in json.load(f)]
