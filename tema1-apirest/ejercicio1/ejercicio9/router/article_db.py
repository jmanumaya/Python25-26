from fastapi import APIRouter, Depends, HTTPException, status
from db.models.article import Article
from db.schemas.article import article_schema, articles_schema
from db.client import db_client
from bson import ObjectId
from .auth_users import authentication 

router = APIRouter(prefix="/articlesdb", tags=["articlesdb"])

# Funciones auxiliares mejoradas
def search_article_title(title: str):
    try:
        article = db_client.newsdb.articles.find_one({"title": title})
        return Article(**article_schema(article)) if article else None
    except:
        return None

def search_article_id(id: str):
    try:
        article = db_client.newsdb.articles.find_one({"_id": ObjectId(id)})
        return Article(**article_schema(article)) if article else None
    except:
        return None

# Endpoints
@router.get("/", response_model=list[Article])
async def get_articles():
    return articles_schema(db_client.newsdb.articles.find())

@router.get("/{id}", response_model=Article)
async def get_article(id: str):
    article = search_article_id(id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.get("/title/{title}", response_model=Article)
async def get_article_by_title(title: str):
    article = search_article_title(title)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.post("/", response_model=Article, status_code=status.HTTP_201_CREATED)
async def add_article(article: Article, authorized: bool = Depends(authentication)):
    if search_article_title(article.title):
        raise HTTPException(status_code=409, detail="Article with this title already exists")

    article_dict = article.model_dump()
    if "id" in article_dict:
        del article_dict["id"]
    
    id = db_client.newsdb.articles.insert_one(article_dict).inserted_id
    
    new_article = article_schema(db_client.newsdb.articles.find_one({"_id": id}))
    return Article(**new_article)

@router.put("/{id}", response_model=Article)
async def modify_article(id: str, article: Article):
    article_dict = article.model_dump()
    if "id" in article_dict:
        del article_dict["id"]
    
    try:
        found = db_client.newsdb.articles.find_one_and_replace({"_id": ObjectId(id)}, article_dict)
        if not found:
            raise HTTPException(status_code=404, detail="Article not found")
        return search_article_id(id)
    except:
         raise HTTPException(status_code=404, detail="Error updating article")

@router.delete("/{id}", response_model=Article)
async def delete_article(id: str):
    try:
        found = db_client.newsdb.articles.find_one_and_delete({"_id": ObjectId(id)})
        if not found:
             raise HTTPException(status_code=404, detail="Article not found")
        return Article(**article_schema(found))
    except:
        raise HTTPException(status_code=404, detail="Invalid ID")