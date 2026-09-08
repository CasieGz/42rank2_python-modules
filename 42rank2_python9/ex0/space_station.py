#!/usr/bin/env python3

# IN THE ROOT
# create venv: python -m venv venv_name
# activate venv: source venv_name/bin/activate
# pip install pydantic flake8 mypy
# show version: python3 -c "import pydantic; print(pydantic.__version__)"

# unpack the tar file with: tar -xf data_generator.tar

from datetime import datetime
try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError as e:
    print(f"\n[WARNING]: {e}")
    print("Install using: pip install pydantic\n")
    exit(1)
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


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    space_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now(),
        is_operational=True
        )
    print("Valid station created:")
    print(f"ID: {space_station.station_id}")
    print(f"Name: {space_station.name}")
    print(f"Crew: {space_station.crew_size} people")
    print(f"Power: {space_station.power_level}%")
    print(f"Oxygen: {space_station.oxygen_level}%")
    # print(f"Datetime: {space_station.last_maintenance}")
    status = "Operational" if space_station.is_operational \
        else "Not Operational"
    print(f"Status: {status}")

    print("\n========================================")
    print("Expected validation error:")
    # date_str = "2026-07-29T09:40:55Z"
    try:
        SpaceStation(
            station_id="AB",
            name="",
            crew_size=25,
            power_level=150.5,
            oxygen_level=-5.0,
            # last_maintenance=datetime.fromisoformat(date_str),
            last_maintenance="invalid",  # type: ignore
            is_operational=False,
            notes="x" * 201
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
