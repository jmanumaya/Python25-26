from fastapi import APIRouter, HTTPException, Depends
from db.models.client import Client
from db.client import db_client
from db.schemas.client import client_schema, clients_schema
from bson import ObjectId
from .auth_users import authentication

router = APIRouter(prefix="/clients", tags=["clients"])


@router.get("/", response_model=list[Client])
async def clients():
    """Obtener todos los clientes"""
    return clients_schema(db_client.gym.clients.find())


@router.get("/trainer/{id_trainer}", response_model=list[Client])
async def clients_by_trainer(id_trainer: str):
    """Obtener todos los clientes de un entrenador específico"""
    return clients_schema(db_client.gym.clients.find({"id_trainer": id_trainer}))


@router.get("/{id}", response_model=Client)
async def client(id: str):
    """Obtener un cliente por ID"""
    return search_client_id(id)


@router.post("/", response_model=Client, status_code=201)
async def add_client(client: Client, authorized=Depends(authentication)):
    """Añadir un nuevo cliente (requiere autenticación)"""
    # Verificamos si el entrenador existe
    try:
        db_client.gym.trainers.find_one({"_id": ObjectId(client.id_trainer)})
    except:
        raise HTTPException(status_code=404, detail="Trainer not found")
    
    # Verificamos si ya existe un cliente con el mismo nombre
    if type(search_client(client.name)) == Client:
        raise HTTPException(status_code=409, detail="Client already exists")
    
    client_dict = client.model_dump()
    del client_dict["id"]
    
    # Añadimos el cliente a la base de datos
    id = db_client.gym.clients.insert_one(client_dict).inserted_id
    client_dict["id"] = str(id)
    
    return Client(**client_dict)


@router.put("/{id}", response_model=Client)
async def modify_client(id: str, new_client: Client, authorized=Depends(authentication)):
    """Modificar un cliente existente (requiere autenticación)"""
    # Verificamos si el nuevo entrenador existe (si se está cambiando)
    try:
        db_client.gym.trainers.find_one({"_id": ObjectId(new_client.id_trainer)})
    except:
        raise HTTPException(status_code=404, detail="Trainer not found")
    
    client_dict = new_client.model_dump()
    del client_dict["id"]
    
    try:
        db_client.gym.clients.find_one_and_replace({"_id": ObjectId(id)}, client_dict)
        return search_client_id(id)
    except:
        raise HTTPException(status_code=404, detail="Client not found")


@router.delete("/{id}", response_model=Client)
async def delete_client(id: str, authorized=Depends(authentication)):
    """Eliminar un cliente (requiere autenticación)"""
    found = db_client.gym.clients.find_one_and_delete({"_id": ObjectId(id)})
    
    if not found:
        raise HTTPException(status_code=404, detail="Client not found")
    return Client(**client_schema(found))


def search_client_id(id: str):
    """Buscar cliente por ID"""
    try:
        client = client_schema(db_client.gym.clients.find_one({"_id": ObjectId(id)}))
        return Client(**client)
    except:
        raise HTTPException(status_code=404, detail="Client not found")


def search_client(name: str):
    """Buscar cliente por nombre"""
    try:
        client = client_schema(db_client.gym.clients.find_one({"name": name}))
        return Client(**client)
    except:
        return {"error": "Client not found"}