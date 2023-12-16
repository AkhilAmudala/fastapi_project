from fastapi import FastAPI
from redis_om import get_redis_connection
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)


redis= get_redis_connection(
    host='redis-15735.c323.us-east-1-2.ec2.cloud.redislabs.com:15735', #publicendpoint_of_DB
    password='yM42M5CXGmNvhM2L7oLlZuzJEmNlUOTr',
    port='11844',
    decode_responses=True
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

#to start server:- "uvicorn main:app --reload"
#to list all running processes in port 8000:- "lsof -i:8000"
#to kill a process:- "kill -9 PID"