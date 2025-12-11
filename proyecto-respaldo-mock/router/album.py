from fastapi import APIRouter, Depends, HTTPException, status
from db.models.album import Album
from db.schemas.album import album_schema, albums_schema
from db.client import db_client
from bson import ObjectId
from .auth_users import authentication

router = APIRouter(prefix="/albumsdb", tags=["albumsdb"])

# ---------- ENDPOINTS ----------

@router.get("/", response_model=list[Album])
async def get_albums():
    # Devuelve todos los artículos de la colección
    return albums_schema(db_client.local.albums.find())


@router.get("/{id}", response_model=Album)
async def get_album(id: str):
    return search_album_id(id)


@router.get("/title/{title}", response_model=Album)
async def get_album_by_title(title: str):
    return search_album_title(title)


@router.get("/release_year/{release_year}", response_model=list[Album])
async def get_albums_by_release_year(release_year: int):
    # Buscamos todos los artículos que coincidan con la fecha
    albums = albums_schema(db_client.local.albums.find({"release_year": release_year}))
    
    if not albums:
        raise HTTPException(status_code=404, detail="No albums found for that date")
    
    return albums


@router.post("/", response_model=Album, status_code=status.HTTP_201_CREATED)
async def add_album(album: Album):
    # Verificamos si ya existe un artículo con el mismo título (opcional)
    if type(search_album_title(album.title)) == Album:
        raise HTTPException(status_code=409, detail="Album with this title already exists")

    album_dict = album.model_dump()
    del album_dict["id"]
    
    # Insertamos en la base de datos
    id = db_client.local.albums.insert_one(album_dict).inserted_id
    
    # Recuperamos el artículo recién creado
    new_album = album_schema(db_client.local.albums.find_one({"_id": id}))
    
    return Album(**new_album)


@router.put("/{id}", response_model=Album)
async def modify_album(id: str, album: Album):
    album_dict = album.model_dump()
    del album_dict["id"]
    
    try:
        # Buscamos y reemplazamos
        db_client.local.albums.find_one_and_replace({"_id": ObjectId(id)}, album_dict)
        # Devolvemos el objeto actualizado usando la función auxiliar
        return search_album_id(id)
    except:
        raise HTTPException(status_code=404, detail="Album not found")


@router.delete("/{id}", response_model=Album)
async def delete_album(id: str):
    try:
        # Buscamos y borramos, guardando el documento borrado en 'found'
        found = db_client.local.albums.find_one_and_delete({"_id": ObjectId(id)})
        
        if not found:
             raise HTTPException(status_code=404, detail="Album not found")
             
        # Devolvemos el objeto que acabamos de borrar (estilo usersdb)
        return Album(**album_schema(found))
    except:
        raise HTTPException(status_code=404, detail="Invalid ID or Album not found")


# ---------- FUNCIONES AUXILIARES (Estilo usersdb) ----------

def search_album_id(id: str):
    try:
        album = album_schema(db_client.local.albums.find_one({"_id": ObjectId(id)}))
        return Album(**album)
    except:
        return {"error": "Album not found"}

def search_album_title(title: str):
    try:
        album = album_schema(db_client.local.articles.find_one({"title": title}))
        return Album(**album)
    except:
        return {"error": "Album not found"}