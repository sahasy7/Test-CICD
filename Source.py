from fastapi import FastAPI
from pydantic import BaseModel
from os import environ as env
import uvicorn
app = FastAPI()

class iteam(BaseModel):
    input_text : str


@app.get("/")
async def root():
    return {"message":"Its working! trial once"}





