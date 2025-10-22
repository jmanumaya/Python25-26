from fastapi import FastAPI, HTTPException
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

@app.get("/journalists")
def get_journalists():
    return list_journalist

@app.get("/journalists/id/{id_journalist}")
def get_journalists_id(id_journalist: int):
    journalists = [journalist for journalist in list_journalist if journalist.id == id_journalist]
    return journalists[0] if journalists else {"error": "journalist not found"}

@app.get("/journalists/dni/{dni_journalist}")
def get_journalists_dni(dni_journalist: str):
    journalists = [journalist for journalist in list_journalist if journalist.dni == dni_journalist]
    return journalists[0] if journalists else {"error": "journalist not found"}

@app.get("/journalists/specialty/{specialty_journalist}")
def get_journalist_by_specialty(specialty_journalist: str):
    result = [journalist for journalist in list_journalist if journalist.specialty == specialty_journalist]
    return result if result else {"error": "journalist not found"}

@app.post("/journalist", status_code=201)
def add_journalist(journalist: Journalist):
    journalist.id = next_id()
    list_journalist.append(journalist)
    return journalist

@app.put("/journalist/{id}", response_model=Journalist)
def modify_journalist(id: int, journalist: Journalist):
    for index, saved_user in enumerate(list_journalist):
        if saved_user.id == id:
            journalist.id = id
            list_journalist[index] = journalist
            return journalist
    
    raise HTTPException(status_code=404, detail="Journalist not found")

@app.delete("/journalist/{id}")
def delete_journalist(id:int):
    for saved_journalist in list_journalist:
        if saved_journalist.id == id:
            list_journalist.remove(saved_journalist)
            return {}
    raise HTTPException(status_code=404, detail="Journalist not found")

def next_id():
    return (max(list_journalist, key=lambda x: x.id).id + 1) if list_journalist else 1
