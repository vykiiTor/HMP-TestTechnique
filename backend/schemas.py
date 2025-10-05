from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

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
