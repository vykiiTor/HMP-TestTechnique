from sqlalchemy.orm import Session
from backend import models, schemas

def get_vulnerabilities(db: Session):
    return db.query(models.Vulnerability).all()

def create_incident(db: Session, incident: schemas.IncidentCreate):
    db_incident = models.Incident(**incident.dict())
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

def update_vulnerability_status(db: Session, vuln_id: int, status: str):
    vuln = db.query(models.Vulnerability).filter(models.Vulnerability.id == vuln_id).first()
    if vuln:
        vuln.status = status
        db.commit()
        db.refresh(vuln)
    return vuln
