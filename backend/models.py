from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend import database

class Vulnerability(database.Base):
    __tablename__ = "vulnerabilities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    severity = Column(String, index=True)   # Critical, High, Medium, Low
    system = Column(String)
    status = Column(String, default="Open") # Open, Closed, In Progress

    incidents = relationship("Incident", back_populates="vulnerability")

class Incident(database.Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    vulnerability_id = Column(Integer, ForeignKey("vulnerabilities.id"))

    vulnerability = relationship("Vulnerability", back_populates="incidents")
