from fastapi import APIRouter, Depends, HTTPException, status
from db.models.colegio import Colegio
from db.schemas.colegio import colegio_schema, colegios_schema
from db.client import db_client
from .auth_users import authentication
from bson import ObjectId

router = APIRouter(prefix="/colegios", tags=["colegiosdb"])

# ---------- ENDPOINTS ----------

@router.get("/", response_model=list[Colegio])
async def get_colegios():
    return colegios_schema(db_client.local.colegios.find())


@router.get("/{id}", response_model=Colegio)
async def get_colegio(id: str):
    return search_colegio_id(id)

# No me da tiempo de la autentificacion pero para que lo sepas tendria que poner al lado de colegio: Colegio, authorized = Depends(authentication) (lo mismo en todas las que necesiten autentificacion)
@router.post("/", response_model=Colegio, status_code=status.HTTP_201_CREATED)
async def add_colegio(colegio: Colegio):
    # Verificamos si existe usando la función auxiliar (por id que es único)
    if type(search_colegio_id(colegio.id)) == Colegio:
        raise HTTPException(status_code=409, detail="Colegio already exists")
    
    if (valida_colegio_tipo(colegio.tipo)):

        # Usamos model_dump()
        colegio_dict = colegio.model_dump()
        del colegio_dict["id"]

        # Insertamos
        id = db_client.local.colegios.insert_one(colegio_dict).inserted_id

        # Recuperamos el objeto creado para devolverlo
        # Usamos la conversión manual de ObjectId a str
        new_colegio = colegio_schema(db_client.local.colegios.find_one({"_id": id}))
        
        return Colegio(**new_colegio)
    
    raise HTTPException(status_code=422, detail="Tipo de colegio no válido")

@router.delete("/{id}", response_model=Colegio)
async def delete_colegio(id: str):
    try:
        found = db_client.local.colegios.find_one_and_delete({"_id": ObjectId(id)})
        if not found:
             raise HTTPException(status_code=404, detail="Colegio not found")
        return Colegio(**colegio_schema(found))
    except:
        raise HTTPException(status_code=404, detail="Invalid ID or Colegio not found")


# ---------- FUNCIONES AUXILIARES ----------

def search_colegio_id(id: str):
    try:
        colegio = colegio_schema(db_client.local.colegios.find_one({"_id": ObjectId(id)}))
        return Colegio(**colegio)
    except:
        return {"error": "Colegio no encontrado"}
    
def valida_colegio_tipo(tipo: str):
    estado = False

    if (str.lower(tipo) == "publico" or str.lower(tipo) == "concertado" or str.lower(tipo) == "privado"):
        estado = True

    return estado