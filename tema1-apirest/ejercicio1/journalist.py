from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator

app = FastAPI()

class Journalist(BaseModel):
    id: int | None = None
    dni: str
    name: str
    surname: str
    telephone: int
    specialty: str

list_journalists = [
    Journalist(id=1, dni="54633722P", name="Descarga", surname="Mapher Game", telephone=765453672, specialty="reporter"),
    Journalist(id=2, dni="44231712T", name="En", surname="Play Store", telephone=987352735, specialty="reporter"),
    Journalist(id=3, dni="24355774M", name="joyagogames", surname=".com", telephone=246374282, specialty="newspaperman")
]


# ---------- FUNCIONES AUXILIARES ----------
def next_id():
    return (max(list_journalists, key=lambda x: x.id).id + 1) if list_journalists else 1

def find_journalist_by_id(id: int):
    return next((j for j in list_journalists if j.id == id), None)


# ---------- ENDPOINTS ----------
@app.get("/journalists", response_model=list[Journalist])
def get_journalists():
    return list_journalists


@app.get("/journalists/{id_journalist}", response_model=Journalist)
def get_journalist_by_id(id_journalist: int):
    journalist = find_journalist_by_id(id_journalist)
    if not journalist:
        raise HTTPException(status_code=404, detail="Journalist not found")
    return journalist


@app.get("/journalists/dni/{dni_journalist}", response_model=Journalist)
def get_journalist_by_dni(dni_journalist: str):
    journalist = next((j for j in list_journalists if j.dni == dni_journalist), None)
    if not journalist:
        raise HTTPException(status_code=404, detail="Journalist not found")
    return journalist


@app.get("/journalists/specialty/{specialty_journalist}", response_model=list[Journalist])
def get_journalist_by_specialty(specialty_journalist: str):
    result = [j for j in list_journalists if j.specialty == specialty_journalist]
    if not result:
        raise HTTPException(status_code=404, detail="No journalists found with that specialty")
    return result


@app.post("/journalists", response_model=Journalist, status_code=201)
def add_journalist(journalist: Journalist):
    journalist.id = next_id()
    list_journalists.append(journalist)
    return journalist


@app.put("/journalists/{id}", response_model=Journalist)
def modify_journalist(id: int, journalist: Journalist):
    for index, saved_journalist in enumerate(list_journalists):
        if saved_journalist.id == id:
            journalist.id = id
            list_journalists[index] = journalist
            return journalist
    raise HTTPException(status_code=404, detail="Journalist not found")


@app.delete("/journalists/{id}", status_code=204)
def delete_journalist(id: int):
    journalist = find_journalist_by_id(id)
    if not journalist:
        raise HTTPException(status_code=404, detail="Journalist not found")
    list_journalists.remove(journalist)
    return