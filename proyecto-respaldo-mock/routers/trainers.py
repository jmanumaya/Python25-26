from fastapi import APIRouter, HTTPException, Depends
from db.models.trainer import Trainer
from db.client import db_client
from db.schemas.trainer import trainer_schema, trainers_schema
from bson import ObjectId
from .auth_users import authentication

router = APIRouter(prefix="/trainers", tags=["trainers"])


@router.get("/", response_model=list[Trainer])
async def trainers():
    """Obtener todos los entrenadores"""
    return trainers_schema(db_client.gym.trainers.find())


@router.get("/{id}", response_model=Trainer)
async def trainer(id: str):
    """Obtener un entrenador por ID"""
    return search_trainer_id(id)


@router.post("/", response_model=Trainer, status_code=201)
async def add_trainer(trainer: Trainer, authorized=Depends(authentication)):
    """Añadir un nuevo entrenador (requiere autenticación)"""
    # Verificamos si ya existe un entrenador con el mismo nombre y especialidad
    if type(search_trainer(trainer.name, trainer.specialty)) == Trainer:
        raise HTTPException(status_code=409, detail="Trainer already exists")
    
    trainer_dict = trainer.model_dump()
    del trainer_dict["id"]
    
    # Añadimos el entrenador a la base de datos
    id = db_client.gym.trainers.insert_one(trainer_dict).inserted_id
    trainer_dict["id"] = str(id)
    
    return Trainer(**trainer_dict)


@router.put("/{id}", response_model=Trainer)
async def modify_trainer(id: str, new_trainer: Trainer, authorized=Depends(authentication)):
    """Modificar un entrenador existente (requiere autenticación)"""
    trainer_dict = new_trainer.model_dump()
    del trainer_dict["id"]
    
    try:
        db_client.gym.trainers.find_one_and_replace({"_id": ObjectId(id)}, trainer_dict)
        return search_trainer_id(id)
    except:
        raise HTTPException(status_code=404, detail="Trainer not found")


@router.delete("/{id}", response_model=Trainer)
async def delete_trainer(id: str, authorized=Depends(authentication)):
    """Eliminar un entrenador (requiere autenticación)"""
    found = db_client.gym.trainers.find_one_and_delete({"_id": ObjectId(id)})
    
    if not found:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return Trainer(**trainer_schema(found))


def search_trainer_id(id: str):
    """Buscar entrenador por ID"""
    try:
        trainer = trainer_schema(db_client.gym.trainers.find_one({"_id": ObjectId(id)}))
        return Trainer(**trainer)
    except:
        raise HTTPException(status_code=404, detail="Trainer not found")


def search_trainer(name: str, specialty: str):
    """Buscar entrenador por nombre y especialidad"""
    try:
        trainer = trainer_schema(db_client.gym.trainers.find_one({"name": name, "specialty": specialty}))
        return Trainer(**trainer)
    except:
        return {"error": "Trainer not found"}