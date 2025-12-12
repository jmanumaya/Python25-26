from fastapi import APIRouter, Depends, HTTPException, status
from db.models.alumno import Alumno
from db.schemas.alumno import alumno_schema, alumnos_schema
from db.models.colegio import Colegio
from db.schemas.colegio import colegio_schema
from db.client import db_client
from bson import ObjectId
from .auth_users import authentication

router = APIRouter(prefix="/alumnos", tags=["alumnosdb"])

# ---------- ENDPOINTS ----------

@router.get("/", response_model=list[Alumno])
async def get_alumnos():
    # Devuelve todos los artículos de la colección
    return alumnos_schema(db_client.local.alumnos.find())


@router.get("/{id}", response_model=Alumno)
async def get_alumno(id: str):
    return search_alumno_id(id)

@router.get("/colegio/{id_colegio}", response_model=list[Alumno])
def get_alumnos_by_colegio(id_colegio: str):
    # Primero compruebo que exista el colegio.
    if type(search_colegio_id(id_colegio)) != Colegio:
        raise HTTPException(status_code=404, detail="No existe el colegio indicado")
    
    # Luego busco los alumnos que tiene (si existe) y los devuelvo tenga o no
    alumnos = []

    for alumno in alumnos_schema(db_client.local.alumnos.find()):
        al = Alumno(**alumno)
        if (al.id_colegio == id_colegio):
            alumnos.append(al)
    return alumnos

# Estos metodos necesitan autentificacion pero te lo comento en el colegios.py el porque no la he puesto y que pondría
@router.post("/", response_model=Alumno, status_code=status.HTTP_201_CREATED)
async def add_alumno(alumno: Alumno):
    # Verificamos si ya existe un colegio con el mismo id
    if type(search_colegio_id(alumno.id_colegio)) == Colegio:

        if (comprueba_alumno_curso(alumno.curso)):
            alumno_dict = alumno.model_dump()
            del alumno_dict["id"]
        
            # Insertamos en la base de datos
            id = db_client.local.alumnos.insert_one(alumno_dict).inserted_id
        
            # Recuperamos el alumno recién creado
            new_alumno = alumno_schema(db_client.local.alumnos.find_one({"_id": id}))
        
            return Alumno(**new_alumno)
        
        raise HTTPException(status_code=422, detail="El curso indicado no es un curso valido (1ESO, 2ESO, 1BACH)")
    
    raise HTTPException(status_code=404, detail="El colegio indicado no existe")


@router.put("/{id}", response_model=Alumno)
async def modify_alumno(id: str, alumno: Alumno):
    alumno_dict = alumno.model_dump()
    del alumno_dict["id"]
    try:
        # Buscamos y reemplazamos
        db_client.local.alumnos.find_one_and_replace({"_id": ObjectId(id)}, alumno_dict)
        # Devolvemos el objeto actualizado usando la función auxiliar
        return search_alumno_id(id)
    except:
        raise HTTPException(status_code=404, detail="Alumno not found")


@router.delete("/{id}", response_model=Alumno)
async def delete_alumno(id: str):
    try:
        # Buscamos y borramos, guardando el documento borrado en 'found'
        found = db_client.local.alumnos.find_one_and_delete({"_id": ObjectId(id)})
        
        if not found:
             raise HTTPException(status_code=404, detail="Alumno not found")
             
        # Devolvemos el objeto que acabamos de borrar
        return Alumno(**alumno_schema(found))
    except:
        raise HTTPException(status_code=404, detail="Invalid ID or Alumno not found")

# ---------- FUNCIONES AUXILIARES ----------

def search_alumno_id(id: str):
    try:
        alumno = alumno_schema(db_client.local.alumnos.find_one({"_id": ObjectId(id)}))
        return Alumno(**alumno)
    except:
        return {"error": "Alumno not found"}
    
def search_colegio_id(id: str):
    try:
        colegio = colegio_schema(db_client.local.colegios.find_one({"_id": ObjectId(id)}))
        return Colegio(**colegio)
    except:
        return {"error": "Colegio no encontrado"}

def comprueba_alumno_curso(curso: str):
    cursos = ["1ESO", "2ESO", "1BACH"]
    estado = False
    if (curso in cursos):
        estado = True
    return estado