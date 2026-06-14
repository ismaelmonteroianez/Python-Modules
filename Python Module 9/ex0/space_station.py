from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def print_station(station: SpaceStation) -> None:
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    if station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Non-operational")
    if station.notes is not None:
        print(f"Notes: {station.notes}")


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    valid_data = {
                    "station_id": "ISS001",
                    "name": "International Space Station",
                    "crew_size": 6,
                    "power_level": 85.5,
                    "oxygen_level": 92.3,
                    "last_maintenance": datetime(2026, 6, 10, 14, 30),
                    "is_operational": True,
                    "notes": None
                }
    try:
        valid_station = SpaceStation(**valid_data)  # type: ignore
        print_station(valid_station)
    except ValidationError as e:
        for err in e.errors():
            error = err["msg"]
            print(error)
    print()
    print("========================================")
    print("Expected validation error:")
    invalid_data = {
                    "station_id": "ISS001",
                    "name": "International Space Station",
                    "crew_size": 21,
                    "power_level": 85.5,
                    "oxygen_level": 92.3,
                    "last_maintenance": datetime(2026, 6, 10, 14, 30),
                    "is_operational": True,
                    "notes": None
                }
    try:
        invalid_station = SpaceStation(**invalid_data)  # type: ignore
        print_station(invalid_station)
    except ValidationError as e:
        for err in e.errors():
            error = err["msg"]
            print(error)


if __name__ == "__main__":
    main()
