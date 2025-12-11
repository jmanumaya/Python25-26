from fastapi import APIRouter, HTTPException, status
from db.models.journalist import Journalist
from db.schemas.journalist import journalist_schema, journalists_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/journalistsdb", tags=["journalistsdb"])

def search_journalist_dni(dni: str):
    try:
        journalist = db_client.newsdb.journalists.find_one({"dni": dni})
        return Journalist(**journalist_schema(journalist)) if journalist else None
    except:
        return None

def search_journalist_id(id: str):
    try:
        journalist = db_client.newsdb.journalists.find_one({"_id": ObjectId(id)})
        return Journalist(**journalist_schema(journalist)) if journalist else None
    except:
        return None

@router.get("/", response_model=list[Journalist])
async def get_journalists():
    return journalists_schema(db_client.newsdb.journalists.find())

@router.get("/{id}", response_model=Journalist)
async def get_journalist(id: str):
    j = search_journalist_id(id)
    if not j:
        raise HTTPException(status_code=404, detail="Journalist not found")
    return j

@router.get("/dni/{dni}", response_model=Journalist)
async def get_journalist_dni(dni: str):
    j = search_journalist_dni(dni)
    if not j:
         raise HTTPException(status_code=404, detail="Journalist not found")
    return j

@router.post("/", response_model=Journalist, status_code=status.HTTP_201_CREATED)
async def add_journalist(journalist: Journalist):
    if search_journalist_dni(journalist.dni):
        raise HTTPException(status_code=409, detail="Journalist already exists")
    
    journalist_dict = journalist.model_dump()
    if "id" in journalist_dict:
        del journalist_dict["id"]

    id = db_client.newsdb.journalists.insert_one(journalist_dict).inserted_id
    
    new_journalist = journalist_schema(db_client.newsdb.journalists.find_one({"_id": id}))
    return Journalist(**new_journalist)

@router.put("/{id}", response_model=Journalist)
async def modify_journalist(id: str, journalist: Journalist):
    journalist_dict = journalist.model_dump()
    if "id" in journalist_dict:
        del journalist_dict["id"]

    try:
        found = db_client.newsdb.journalists.find_one_and_replace({"_id": ObjectId(id)}, journalist_dict)
        if not found:
            raise HTTPException(status_code=404, detail="Journalist not found")
        return search_journalist_id(id)
    except:
        raise HTTPException(status_code=404, detail="Journalist not found")

@router.delete("/{id}", response_model=Journalist)
async def delete_journalist(id: str):
    try:
        found = db_client.newsdb.journalists.find_one_and_delete({"_id": ObjectId(id)})
        if not found:
             raise HTTPException(status_code=404, detail="Journalist not found")
        return Journalist(**journalist_schema(found))
    except:
        raise HTTPException(status_code=404, detail="Invalid ID")