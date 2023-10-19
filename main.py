import fastapi

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class DataItem(BaseModel):
    data: list


@app.get("/get_formatted_data")
def receive_data(item: DataItem):
    data = item.data
    return {"message": "Data received successfully"}


@app.get("/")
async def root():
    return {"message": "Hello World"}
