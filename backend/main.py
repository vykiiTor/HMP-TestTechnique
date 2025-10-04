from unittest import skipIf

from fastapi import FastAPI, HTTPException

api = FastAPI()



#GET
@api.get('/')
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
    pass
