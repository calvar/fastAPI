from typing import List
from fastapi import FastAPI, HTTPException
import json

from models import Record, Category

#Application
app = FastAPI()

#Load database
In = open("simple_data.json")
db = json.load(In)
In.close()

#print(db)

#Main endpoint
@app.get('/')
async def root():
    return "Hello!"

#Database endpoint
@app.get('/api/v1/database')
async def get_records(indexes: str):
    data = []
    for index in indexes.split(','):
        rec = {}
        for col in db:
            rec[col] = db[col][str(index)]
        data.append(rec)
    return data

