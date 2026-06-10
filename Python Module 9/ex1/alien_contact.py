from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Optional


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact(self) -> None:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and self.is_verified is False:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) must include a message")
        return self


def print_contact(contact: AlienContact) -> None:
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received is not None:
        print(f"Message: {contact.message_received}")


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    valid_data = {
                    "contact_id": "AC_2024_001",
                    "timestamp": datetime(2026, 6, 10, 14, 30),
                    "location": "Area 51, Nevada",
                    "contact_type": ContactType.radio,
                    "signal_strength": 8.5,
                    "duration_minutes": 45,
                    "witness_count": 5,
                    "message_received": "Greetings from Zeta Reticuli",
                    "is_verified": False
                }
    try:
        valid_contact = AlienContact(**valid_data)  # type: ignore
        print_contact(valid_contact)
    except ValidationError as e:
        for err in e.errors():
            error = err["msg"]
            print(error)
    print()
    print("======================================")
    print("Expected validation error:")
    invalid_data = {
                    "contact_id": "C_2024_001",
                    "timestamp": datetime(2026, 6, 10, 14, 30),
                    "location": "Area 51, Nevada",
                    "contact_type": ContactType.radio,
                    "signal_strength": 8.5,
                    "duration_minutes": 45,
                    "witness_count": 5,
                    "message_received": "Greetings from Zeta Reticuli",
                    "is_verified": False
                }
    try:
        invalid_contact = AlienContact(**invalid_data)  # type: ignore
        print_contact(invalid_contact)
    except ValidationError as e:
        for err in e.errors():
            error = err["msg"]
            print(error)


if __name__ == "__main__":
    main()
