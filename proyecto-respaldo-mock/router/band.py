from fastapi import APIRouter, HTTPException, status
from db.models.band import Band
from db.schemas.band import band_schema, bands_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/bandsdb", tags=["bandsdb"])

# ---------- ENDPOINTS ----------

@router.get("/", response_model=list[Band])
async def get_bands():
    return bands_schema(db_client.local.bands.find())


@router.get("/{id}", response_model=Band)
async def get_band(id: str):
    return search_band_id(id)


@router.get("/name/{name}", response_model=Band)
async def get_band_name(name: str):
    return search_band_name(name)


@router.post("/", response_model=Band, status_code=status.HTTP_201_CREATED)
async def add_band(band: Band):
    # Verificamos si existe usando la función auxiliar (por DNI que es único)
    if type(search_band_name(band.name)) == Band:
        raise HTTPException(status_code=409, detail="Band already exists")
    
    band_dict = band.model_dump()
    del band_dict["id"]

    # Insertamos
    id = db_client.local.bands.insert_one(band_dict).inserted_id

    # Recuperamos el objeto creado para devolverlo
    # Usamos la conversión manual de ObjectId a str
    new_band = band_schema(db_client.local.bands.find_one({"_id": id}))
    
    return Band(**new_band)


@router.put("/{id}", response_model=Band)
async def modify_band(id: str, band: Band):
    band_dict = band.model_dump()
    del band_dict["id"]

    try:
        # Buscamos y reemplazamos
        db_client.local.bands.find_one_and_replace({"_id": ObjectId(id)}, band_dict)
        # Devolvemos el objeto buscándolo de nuevo
        return search_band_id(id)
    except:
        raise HTTPException(status_code=404, detail="Band not found")


@router.delete("/{id}", response_model=Band)
async def delete_band(id: str):
    try:
        found = db_client.local.bands.find_one_and_delete({"_id": ObjectId(id)})
        if not found:
             raise HTTPException(status_code=404, detail="Band not found")
        return Band(**band_schema(found))
    except:
        raise HTTPException(status_code=404, detail="Invalid ID or Band not found")


# ---------- FUNCIONES AUXILIARES (Estilo usersdb) ----------

def search_band_id(id: str):
    try:
        band = band_schema(db_client.local.bands.find_one({"_id": ObjectId(id)}))
        return Band(**band)
    except:
        return {"error": "Band not found"}

def search_band_name(name: str):
    try:
        band = band_schema(db_client.local.bands.find_one({"name": name}))
        return Band(**band)
    except:
        return {"error": "Band not found"}