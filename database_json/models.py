#BaseModel is has the base requirements for an endpoint
from pydantic import BaseModel
from typing import Optional, List #Enforce types
from enum import Enum

class Category(str, Enum):
    A = "a"
    B = "b"


class Record(BaseModel):
    C1: int
    C2: Category
    C3: float

