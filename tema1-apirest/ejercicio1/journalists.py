from fastapi import FastAPI
from pydantic import BaseModel

class Journalist(BaseModel):
    id:int
    dni:str
    name:str
    surname:str
    telephone:int
    specialty:str

list_journalist = [Journalist(id = 1, dni = "54633722P", name = "Descarga", surname = "Mapher Game", telephone = 765453672, specialty = "reporter"),
              Journalist(id = 2, dni = "44231712T", name = "En", surname = "Play Store", telephone = 987352735, specialty = "reporter"),
              Journalist(id = 3, dni = "24355774M", name = "joyagogames", surname = ".com", telephone = 246374282, specialty = "newspaperman")]

app = FastAPI()

@app.get("/")
def get_journalists():
    return list_journalist

@app.get("/journalist/id/{id_journalist}")
def get_journalists_id(id_journalist: int):
    journalists = [journalist for journalist in list_journalist if journalist.id == id_journalist]
    return journalists[0] if journalists else {"error": "journalist not found"}

@app.get("/journalist/dni/{dni_journalist}")
def get_journalists_dni(dni_journalist: str):
    journalists = [journalist for journalist in list_journalist if journalist.dni == dni_journalist]
    return journalists[0] if journalists else {"error": "journalist not found"}

@app.get("/journalist/specialty/{specialty_journalist}")
def get_journalist_by_specialty(specialty_journalist: str):
    result = [j for j in list_journalist if j.specialty == specialty_journalist]
    return result if result else {"error": "journalist not found"}