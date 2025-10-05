from fastapi import FastAPI, HTTPException
from backend import models, database, logicValidation, schemas, endPoints

models.database.Base.metadata.create_all(bind=database.engine)
api = FastAPI()
api.include_router(endPoints.router)

'''@api.get('/')
def index():
    return {"message" : 'hello world'}

#GET vulnerabilities
@api.get('/vulnerabilities')
def get_vulnerabilites():
    return {"message" : 'hello world'}

#POST new incident
@api.post('/incident')
def post_incident():
    return {"message" : 'hello world'}

#PUT change status
@api.put('/vulnerabilities/{vul_id}/status')
def put_status(vul_id: int, new_status: dict):
    pass'''
