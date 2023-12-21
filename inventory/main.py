from fastapi import FastAPI
from redis import RedisError
from redis_om import get_redis_connection, HashModel, redis
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from pydantic import BaseModel


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8000'],
    allow_methods=['*'],
    allow_headers=['*']
)

import redis

r = redis.Redis(
  host='redis-15735.c323.us-east-1-2.ec2.cloud.redislabs.com', port=15735, password='yM42M5CXGmNvhM2L7oLlZuzJEmNlUOTr',decode_responses=True)

# redis= get_redis_connection(
#     host='redis-15735.c323.us-east-1-2.ec2.cloud.redislabs.com:15735', #publicendpoint_of_DB
#     password='yM42M5CXGmNvhM2L7oLlZuzJEmNlUOTr',
#     port='15735', #get this from redis DB connection: https://app.redislabs.com/#/databases/12058748/subscription/2220215/view-bdb/configuration
#     decode_responses=True
# )
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
        database=r
#now whatever product we create will be stored in redis        

@app.get('/products')
def all():
    return [format(i) for i in Product.all_pks()] #to return all products in  redis

@app.post('/products')
def create(product: Product):
    product.save()
    return {"message": "Product created successfully"}


#to start server from main fodler directory:- "uvicorn main:app --reload"
#to list all running processes in port 8000:- "lsof -i:8000"
#to kill a process:- "kill -9 PID"