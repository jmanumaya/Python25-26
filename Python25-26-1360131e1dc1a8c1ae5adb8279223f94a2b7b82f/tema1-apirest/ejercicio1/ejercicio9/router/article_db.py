from fastapi import APIRouter, Depends, HTTPException, status
from db.models.article import Article
from db.schemas.article import article_schema, articles_schema
from db.client import db_client
from bson import ObjectId
from .auth_users import authentication

router = APIRouter(prefix="/articlesdb", tags=["articlesdb"])

# ---------- ENDPOINTS ----------

@router.get("/", response_model=list[Article])
async def get_articles():
    # Devuelve todos los artículos de la colección
    return articles_schema(db_client.local.articles.find())


@router.get("/{id}", response_model=Article)
async def get_article(id: str):
    return search_article_id(id)


@router.get("/title/{title}", response_model=Article)
async def get_article_by_title(title: str):
    return search_article_title(title)


@router.get("/date/{date}", response_model=list[Article])
async def get_articles_by_date(date: str):
    # Buscamos todos los artículos que coincidan con la fecha
    articles = articles_schema(db_client.local.articles.find({"date": date})) # CUIDADO QUE EL date azulito es el parametro de entrada (date: str)
    
    if not articles:
        raise HTTPException(status_code=404, detail="No articles found for that date")
    
    return articles


@router.post("/", response_model=Article, status_code=status.HTTP_201_CREATED)
async def add_article(article: Article, authorized: bool = Depends(authentication)):
    # Verificamos si ya existe un artículo con el mismo título (opcional)
    if type(search_article_title(article.title)) == Article:
        raise HTTPException(status_code=409, detail="Article with this title already exists")

    article_dict = article.model_dump()
    del article_dict["id"]
    
    # Insertamos en la base de datos
    id = db_client.local.articles.insert_one(article_dict).inserted_id
    
    # Recuperamos el artículo recién creado
    new_article = article_schema(db_client.local.articles.find_one({"_id": id}))
    
    return Article(**new_article)


@router.put("/{id}", response_model=Article)
async def modify_article(id: str, article: Article):
    article_dict = article.model_dump()
    del article_dict["id"]
    
    try:
        # Buscamos y reemplazamos
        db_client.local.articles.find_one_and_replace({"_id": ObjectId(id)}, article_dict)
        # Devolvemos el objeto actualizado usando la función auxiliar
        return search_article_id(id)
    except:
        raise HTTPException(status_code=404, detail="Article not found")


@router.delete("/{id}", response_model=Article)
async def delete_article(id: str):
    try:
        # Buscamos y borramos, guardando el documento borrado en 'found'
        found = db_client.local.articles.find_one_and_delete({"_id": ObjectId(id)})
        
        if not found:
             raise HTTPException(status_code=404, detail="Article not found")
             
        # Devolvemos el objeto que acabamos de borrar (estilo usersdb)
        return Article(**article_schema(found))
    except:
        raise HTTPException(status_code=404, detail="Invalid ID or Article not found")


# ---------- FUNCIONES AUXILIARES (Estilo usersdb) ----------

def search_article_id(id: str):
    try:
        article = article_schema(db_client.local.articles.find_one({"_id": ObjectId(id)}))
        return Article(**article)
    except:
        return {"error": "Article not found"}

def search_article_title(title: str):
    try:
        article = article_schema(db_client.local.articles.find_one({"title": title}))
        return Article(**article)
    except:
        return {"error": "Article not found"}