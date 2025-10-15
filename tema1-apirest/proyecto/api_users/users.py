from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id:int
    name:str
    surname:str
    age:int

users_list = [User(id = 1, name = "Mapher Game", surname = "Descarga", age = 20),
              User(id = 2, name = "En", surname = "Play Store", age = 20),
              User(id = 3, name = "JoseMa", surname = "Maya", age = 20)]

@app.get("/users/{id_user}")
def get_user(id_user: int):
    users = [user for user in users_list if user.id == id_user]

    return users[0] if len(users) != 0 else {"error: user not found"}

