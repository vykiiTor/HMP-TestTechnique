from fastapi import FastAPI
from backend import models, database, logicValidation, schemas, endPoints
from fastapi.middleware.cors import CORSMiddleware

models.database.Base.metadata.create_all(bind=database.engine)
api = FastAPI()


api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
