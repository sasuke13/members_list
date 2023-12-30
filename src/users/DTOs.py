from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class UserDTO:
    name: str
    surname: str
    age: str
    id: Optional[int] = None
