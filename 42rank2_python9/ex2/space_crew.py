#!/usr/bin/env python3

from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Self


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_safety_requirements(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        if not any(
            member.rank in (Rank.CAPTAIN, Rank.COMMANDER)
                for member in self.crew):
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            experienced_members = sum(
                1 for m in self.crew if m.years_experience > 5
            )
            if experienced_members / len(self.crew) < 0.5:
                raise ValueError(
                    r"Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)")
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")
        return self


def print_mission_summary(mission: SpaceMission) -> None:
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions:.1f}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    valid_crew = [
        CrewMember(
            member_id="M01",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=40,
            specialization="Mission Command",
            years_experience=10
        ),
        CrewMember(
            member_id="M02",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=32,
            specialization="Navigation",
            years_experience=6
        ),
        CrewMember(
            member_id="M03",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=29,
            specialization="Engineering",
            years_experience=2
        ),
    ]

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=valid_crew
        )
        print_mission_summary(valid_mission)
    except ValidationError as e:
        error_msg = e.errors()[0]["msg"].replace("Value error, ", "")
        print(error_msg)

    print("\n=========================================")
    print("Expected validation error:")

    invalid_crew = [
        CrewMember(
            member_id="M02",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=32,
            specialization="Navigation",
            years_experience=2,
            is_active=False
        )
    ]

    try:
        SpaceMission(
            mission_id="X2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500.0,
            crew=invalid_crew
        )
    except ValidationError as e:
        for error in e.errors():
            msg = error["msg"].replace("Value error, ", "")
            print(msg)


if __name__ == "__main__":
    main()
