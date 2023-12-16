from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#to start server:- "uvicorn main:app --reload"
#to list all running processes in port 8000:- "lsof -i:8000"
#to kill a process:- "kill -9 PID"

