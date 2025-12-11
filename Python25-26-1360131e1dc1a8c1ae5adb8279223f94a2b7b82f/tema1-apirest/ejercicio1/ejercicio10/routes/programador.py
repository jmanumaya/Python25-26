from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/programmer", tags=["Programmer"])

class Programmer(BaseModel):
    id: int
    dni: str
    name: str
    surname: str
    telephone: int
    email: str

list_programmer = [
    Programmer(id=1, dni="12345678A", name="Carlos", surname="García", telephone=611223344, email="carlos.garcia@example.com"),
    Programmer(id=2, dni="87654321B", name="Laura", surname="Martínez", telephone=622334455, email="laura.martinez@example.com"),
    Programmer(id=3, dni="11223344C", name="Andrés", surname="López", telephone=633445566, email="andres.lopez@example.com"),
    Programmer(id=4, dni="44332211D", name="Sofía", surname="Ruiz", telephone=644556677, email="sofia.ruiz@example.com"),
    Programmer(id=5, dni="55667788E", name="Diego", surname="Fernández", telephone=655667788, email="diego.fernandez@example.com")
]

# ------------ FUNCIONES AUXILIARES -------------
def next_id():
    return (max(list_programmer, key=lambda x: x.id).id + 1) if list_programmer else 1

def find_programmer_by_id(id: int):
    return next((p for p in list_programmer if p.id == id), None)

# ------------ ENDPOINTS ------------
@router.get("/", response_model=list[Programmer])
def get_programmer():
    return list_programmer

@router.get("/{id}", response_model=Programmer)
def get_programmer_by_id(id: int):
    programmer = find_programmer_by_id(id)
    if not programmer:
        raise HTTPException(status_code=404, detail="Programmer not fount")
    return programmer

@router.get("/dni/{dni}", response_model=Programmer)
def get_programmer_by_dni(dni:str):
    programmer = next((p for p in list_programmer if p.dni == dni), None)
    if not programmer:
        raise HTTPException(status_code=404, detail="Programmer not found")
    return programmer

@router.get("/telephone/{tel}", response_model=Programmer)
def get_programmer_by_telephone(tel:int):
    programmer = next((p for p in list_programmer if p.telephone == tel), None)
    if not programmer:
        raise HTTPException(status_code=404, detail="Programmer not found")
    return programmer

@router.post("", response_model=Programmer, status_code=201)
def add_programmer(programmer: Programmer):
    programmer.id = next_id()
    list_programmer.append(programmer)
    return programmer

@router.put("/{id}", response_model=Programmer)
def modify_programmer(id: int, programmer: Programmer):
    for index, saved_programmer in enumerate(list_programmer):
        if saved_programmer.id == id:
            programmer.id = id
            list_programmer[index] = programmer
            return programmer
    raise HTTPException(status_code=404, detail="Programmer not found")

@router.delete("/{id}", status_code=204)
def delete_programmer(id:int):
    programmer = find_programmer_by_id(id)
    if not programmer:
        raise HTTPException(status_code=404, detail="Programmer not found")
    list_programmer.remove(programmer)
    return