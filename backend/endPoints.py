from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend import logicValidation, schemas, database


'''
3 endpoints 
no logic here because of somewhat good archi
the response is the from schema vuls and inci but not had typed controlled
'''
router = APIRouter()

@router.get("/vulnerabilities", response_model=list[schemas.Vulnerability])
def read_vulnerabilities(db: Session = Depends(database.get_db)):
    return logicValidation.get_vulnerabilities(db)

@router.put("/vulnerabilities/{vuln_id}/status", response_model=schemas.Vulnerability)
def update_status(vuln_id: int, status: str, db: Session = Depends(database.get_db)):
    return logicValidation.update_vulnerability_status(db, vuln_id, status)


@router.post("/incidents", response_model=schemas.Incident)
def create_incident(incident: schemas.IncidentCreate, db: Session = Depends(database.get_db)):
    return logicValidation.create_incident(db, incident)