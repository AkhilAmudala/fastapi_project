from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
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

#storing data in Redis as hashes, can use JSONModel also
class Product(HashModel):
    name: str
    price: float
    quantity: int
    #to connect product class to redis database -> Meta class

    class Meta:
        database=redis
#now whatever product we create will be stored in redis        

#to start server:- "uvicorn main:app --reload"
#to list all running processes in port 8000:- "lsof -i:8000"
#to kill a process:- "kill -9 PID"