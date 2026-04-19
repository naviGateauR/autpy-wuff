from dataclasses import dataclass, field
from enum import Enum


class SexEnum(Enum):
    MALE = "männlich"
    FEMALE = "weiblich"


@dataclass
class Dog:
    name: str
    birth_year: int
    sex: SexEnum