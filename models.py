#BaseModel is has the base requirements for an endpoint
from pydantic import BaseModel 
from typing import Optional, List #Enforce types
from uuid import UUID, uuid4 #Generate universal unique identifiers
from enum import Enum


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"

class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    STUDENT = "student"
    
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]
