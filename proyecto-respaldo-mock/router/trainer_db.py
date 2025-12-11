from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth_users import auth_user
from db.models.trainer import Trainer
from db.client import db_client
from db.schemas.trainer import trainer_schema, trainers_schema

from bson import ObjectId

router = APIRouter(prefix="/trainersdb", tags=["trainersdb"])

# la siguiente lista pretende simular una base de datos para probar nuestra API
trainers_list = []

@router.get("/", response_model=list[Trainer])
async def trainers():
    # El método find() sin parámetros devuelve todos los registros
    # de la base de datos
    return trainers_schema(db_client.test.trainers.find())

# Método get tipo query. Sólo busca por id
@router.get("", response_model=Trainer)
async def trainer(id: str):
    return search_trainer_id(id)


# Método get por id
@router.get("/{id}", response_model=Trainer)
async def trainer(id: str):
    return search_trainer_id(id)


@router.post("/", response_model=Trainer, status_code=201)
async def add_trainer(trainer: Trainer):
    #print("dentro de post")
    if type(search_trainer(trainer.name, trainer.surname)) == Trainer:
        raise HTTPException(status_code=409, detail="Trainer already exists")
    
    trainer_dict = trainer.model_dump()
    del trainer_dict["id"]
    # Añadimos el usuario a nuestra base de datos
    # También podemos obtner con inserted_id el id que la base de datos
    # ha generado para nuestro usuario
    id= db_client.test.trainers.insert_one(trainer_dict).inserted_id

    # Añadimos el campo id a nuestro diccionario. Hay que hacerle un cast
    # a string puesto que el id en base de datos se almacena como un objeto,
    # no como un string
    trainer_dict["id"] = str(id)

    # La respuesta de nuestro método es el propio usuario añadido
    # Creamos un objeto de tipo Trainer a partir del diccionario trainer_dict
    return Trainer(**trainer_dict)
    
@router.put("/{id}", response_model=Trainer)
async def modify_trainer(id: str, new_trainer: Trainer):
    # Convertimos el usuario a un diccionario
    trainer_dict = new_trainer.model_dump()
    # Eliminamos el id en caso de que venga porque no puede cambiar
    del trainer_dict["id"]   
    try:
        # Buscamos el id en la base de datos y le pasamos el diccionario con los datos
        # a modificar del usuario
        db_client.test.trainers.find_one_and_replace({"_id":ObjectId(id)}, trainer_dict)
        # Buscamos el objeto en base de datos y lo retornamos, así comprobamos que efectivamente
        # se ha modificado
        return search_trainer_id(id)    
    except:
        raise HTTPException(status_code=404, detail="Trainer not found")
    

@router.delete("/{id}", response_model=Trainer)
async def delete_trainer(id:str):
    found = db_client.test.trainers.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return Trainer(**trainer_schema(found))
   
# El id de la base de datos es un string, ya no es un entero
def search_trainer_id(id: str):    
    # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
    # así que la controlamos
    try:
        # El id en base de datos no se guarda como un string, sino que es un objeto 
        # Realizamos la conversión    
        trainer = trainer_schema(db_client.test.trainers.find_one({"_id":ObjectId(id)}))
        # Necesitamos convertirlo a un objeto Trainer. 
        return Trainer(**trainer)
    except:
        return {"error": "Trainer not found"}



def search_trainer(name: str, surname: str):
    # La búsqueda me devuelve un objeto del tipo de la base de datos.
    # Necesitamos convertirlo a un objeto Trainer. 
    try:
        # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
        # así que la controlamos
        trainer = trainer_schema(db_client.test.trainers.find_one({"name":name, "surname":surname}))
        return Trainer(**trainer)
    except:
        return {"error": "Trainer not found"}


def next_id():
    # Calculamos el usuario con el id más alto 
    # y le sumamos 1 a su id
    return (max(trainer.id for trainer in trainers_list))+1