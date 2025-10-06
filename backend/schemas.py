from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import IntEnum

class IncidentBase(BaseModel):
    description: str
    vulnerability_id: int

class IncidentCreate(IncidentBase):
    pass

class Incident(IncidentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class VulnerabilityBase(BaseModel):
    name: str
    severity: str
    system: str
    status: str = "Open"

class VulnerabilityCreate(VulnerabilityBase):
    pass

class Vulnerability(VulnerabilityBase):
    id: int
    incidents: List[Incident] = []

    class Config:
        orm_mode = True

#classification of the severity TODO
class Severity(IntEnum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW =4