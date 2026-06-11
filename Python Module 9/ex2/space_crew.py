from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le= 10000.0)

    @model_validator(mode="after")
    def validate_mission(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")
        has_leader=False
        for member in self.crew:
            if member.rank == Rank.commander or member.rank == Rank.captain:
                has_leader = True
        if has_leader is False:
            raise ValueError("Mission must have at least one Commander or Captain")
        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")
        if self.duration_days > 365:
            experienced = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced += 1
            if experienced < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) need 50% experienced crew (5+ years)")
        return self


def print_mission(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) - {member.specialization}")

def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    valid_crew = [
    CrewMember(
        member_id="A001",
        name="Sarah Connor",
        rank=Rank.commander,
        age=40,
        specialization="Leadership",
        years_experience=15,
        is_active=True
    ),
    CrewMember(
        member_id="A002",
        name="John Smith",
        rank=Rank.lieutenant,
        age=32,
        specialization="Navigation",
        years_experience=6,
        is_active=True
    ),
    CrewMember(
        member_id="A003",
        name="Alice Johnson",
        rank=Rank.officer,
        age=28,
        specialization="Engineering",
        years_experience=3,
        is_active=True
    ),
    CrewMember(
        member_id="A004",
        name="John Smith",
        rank=Rank.captain,
        age=38,
        specialization="Navigation",
        years_experience=12,
        is_active=True
    ),
    CrewMember(
        member_id="A005",
        name="Mark Davis",
        rank=Rank.lieutenant,
        age=34,
        specialization="Systems",
        years_experience=8,
        is_active=True
    )
    ]
    valid_data = {"mission_id": "M2024_MARS",
                     "mission_name": "Mars Colony Establishment",
                     "destination": "Mars",
                     "launch_date": datetime(2026, 6, 10, 14, 30),
                     "duration_days": 900,
                     "crew": valid_crew,
                     "mission_status": "planned",
                     "budget_millions": 2500
                     }
    try:
        valid_mission = SpaceMission(**valid_data)
        print_mission(valid_mission)
    except ValidationError as e:
        for err in e.errors():
            error = err["msg"]
            print(error)
    print()
    print("=========================================")
    print("Expected validation error:")
    invalid_crew = [
    CrewMember(
        member_id="A001",
        name="Sarah Connor",
        rank=Rank.commander,
        age=40,
        specialization="Leadership",
        years_experience=15,
        is_active=True
    ),
    CrewMember(
        member_id="A002",
        name="John Smith",
        rank=Rank.lieutenant,
        age=32,
        specialization="Navigation",
        years_experience=6,
        is_active=True
    ),
    CrewMember(
        member_id="A003",
        name="Alice Johnson",
        rank=Rank.officer,
        age=28,
        specialization="Engineering",
        years_experience=3,
        is_active=True
    ),
    CrewMember(
        member_id="A004",
        name="John Smith",
        rank=Rank.captain,
        age=38,
        specialization="Navigation",
        years_experience=1,
        is_active=True
    ),
    CrewMember(
        member_id="A005",
        name="Mark Davis",
        rank=Rank.lieutenant,
        age=34,
        specialization="Systems",
        years_experience=3,
        is_active=True
    )
    ]
    invalid_data = {"mission_id": "M2024_MARS",
                     "mission_name": "Mars Colony Establishment",
                     "destination": "Mars",
                     "launch_date": datetime(2026, 6, 10, 14, 30),
                     "duration_days": 900,
                     "crew": invalid_crew,
                     "mission_status": "planned",
                     "budget_millions": 2500
                     }
    try:
        invalid_mission = SpaceMission(**invalid_data)
        print_mission(invalid_mission)
    except ValidationError as e:
        for err in e.errors():
            error = err["msg"]
            print(error)

if __name__ == "__main__":
    main()
