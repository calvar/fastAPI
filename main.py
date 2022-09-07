#Run with$ uvicorn main:app --reload
# This should launch the api on localhost/8000 by default
#FastAPI generates documentation automatically!!!!
# The documentation is on the main endpoint, in this case:
# localhost/800/docs
from typing import List
from fastapi import FastAPI, HTTPException
from uuid import UUID

from models import User, UpdateUser, Gender, Role


#Application
app = FastAPI() 

#Database
db: List[User] = [
    User(id=UUID("5c4c09df-728d-46ae-8f88-0305b334924c"),
         first_name="Camila",
         last_name = "Contreras",
         gender = Gender.FEMALE,
         roles = [Role.STUDENT]
    ),
    User(id=UUID("cd6ca7de-b517-4803-aa2b-d54917175c33"),
         first_name = "Alex",
         last_name = "Jones",
         gender = Gender.MALE,
         roles = [Role.ADMIN, Role.USER]
    )
]


#Main endpoint------------------------------------
@app.get('/')
async def root(): #async means that the program will not wait for the function to finish befoer continuing
    return {"Hello": "Mundo"}

#Users endpoint-----------------------------------
@app.get('/api/v1/users')
async def fetch_users():
    return db;

@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )
    
@app.put('/api/v1/users/{user_id}')
async def update_user(update_info: UpdateUser, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if update_info.first_name is not None:
                user.first_name = update_info.first_name
            if update_info.last_name is not None:
                user.last_name = update_info.last_name
            if update_info.middle_name is not None:
                user.middle_name = update_info.middle_name
            if update_info.roles is not None:
                user.roles = update_info.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )
