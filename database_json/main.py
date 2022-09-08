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

print(len(db))

#Main endpoint
@app.get('/')
async def root():
    return "Hello!"

#Database endpoint
@app.get('/api/v1/database')
async def get_records(indexes: str):
    indxs = indexes.split(',')
    if indxs[0] == '':
        indxs = [str(i) for i in range(len(db["C1"]))]
    data = []
    for index in indxs:
        rec = {}
        for col in db:
            rec[col] = db[col][str(index)]
        data.append(rec)
    return data
    

@app.post('/api/v1/database')
async def add_records(new_data: List[Record]):
    for rec in new_data:
        for col in db:
            db[col][str(len(db[col]))] = dict(rec)[col]
    return


