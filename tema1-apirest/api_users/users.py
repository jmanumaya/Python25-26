from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list = [
    User(id=1, name="Mapher Game", surname="Descarga", age=20),
    User(id=2, name="En", surname="Play Store", age=20),
    User(id=3, name="JoseMa", surname="Maya", age=20)
]


@app.get("/users")
def get_users():
    """Devuelve toda la lista de usuarios"""
    return users_list


@app.get("/users/{id_user}")
def get_user_by_id(id_user: int):
    """Devuelve un usuario por su ID desde la ruta"""
    return search_user(id_user)


@app.post("/users/")
def get_user(id: int):
    return search_user(id)


def search_user(id: int):
    """Función auxiliar para buscar un usuario por su ID"""
    users = [user for user in users_list if user.id == id]
    if users:
        return users[0]
    return {"error": "user not found"}
