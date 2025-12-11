from fastapi import APIRouter, HTTPException, status
from db.models.journalist import Journalist
from db.schemas.journalist import journalist_schema, journalists_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/journalistsdb", tags=["journalistsdb"])

# ---------- ENDPOINTS ----------

@router.get("/", response_model=list[Journalist])
async def get_journalists():
    # Usamos db_client y el esquema plural
    # Asumo que usas la base de datos 'local', si usas 'test' cámbialo aquí
    return journalists_schema(db_client.local.journalists.find())


@router.get("/{id}", response_model=Journalist)
async def get_journalist(id: str):
    return search_journalist_id(id)


@router.get("/dni/{dni}", response_model=Journalist)
async def get_journalist_dni(dni: str):
    return search_journalist_dni(dni)


@router.post("/", response_model=Journalist, status_code=status.HTTP_201_CREATED)
async def add_journalist(journalist: Journalist):
    # Verificamos si existe usando la función auxiliar (por DNI que es único)
    if type(search_journalist_dni(journalist.dni)) == Journalist:
        raise HTTPException(status_code=409, detail="Journalist already exists")
    
    # Usamos model_dump() como en tu ejemplo (Pydantic v2)
    journalist_dict = journalist.model_dump()
    del journalist_dict["id"]

    # Insertamos
    id = db_client.local.journalists.insert_one(journalist_dict).inserted_id

    # Recuperamos el objeto creado para devolverlo
    # Usamos la conversión manual de ObjectId a str
    new_journalist = journalist_schema(db_client.local.journalists.find_one({"_id": id}))
    
    return Journalist(**new_journalist)


@router.put("/{id}", response_model=Journalist)
async def modify_journalist(id: str, journalist: Journalist):
    journalist_dict = journalist.model_dump()
    del journalist_dict["id"]

    try:
        # Buscamos y reemplazamos
        db_client.local.journalists.find_one_and_replace({"_id": ObjectId(id)}, journalist_dict)
        # Devolvemos el objeto buscándolo de nuevo
        return search_journalist_id(id)
    except:
        raise HTTPException(status_code=404, detail="Journalist not found")


@router.delete("/{id}", response_model=Journalist)
async def delete_journalist(id: str):
    try:
        found = db_client.local.journalists.find_one_and_delete({"_id": ObjectId(id)})
        if not found:
             raise HTTPException(status_code=404, detail="Journalist not found")
        return Journalist(**journalist_schema(found))
    except:
        raise HTTPException(status_code=404, detail="Invalid ID or Journalist not found")


# ---------- FUNCIONES AUXILIARES (Estilo usersdb) ----------

def search_journalist_id(id: str):
    try:
        journalist = journalist_schema(db_client.local.journalists.find_one({"_id": ObjectId(id)}))
        return Journalist(**journalist)
    except:
        return {"error": "Journalist not found"}

def search_journalist_dni(dni: str):
    try:
        journalist = journalist_schema(db_client.local.journalists.find_one({"dni": dni}))
        return Journalist(**journalist)
    except:
        return {"error": "Journalist not found"}