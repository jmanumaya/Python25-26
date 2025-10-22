from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Article(BaseModel):
    id:int
    title:str
    body:str
    date:str
    idJournalist:int

article_list = [
    Article(
        id=1,
        title="El auge de los videojuegos indie",
        body="Cada vez más desarrolladores independientes logran destacar gracias a la innovación y el apoyo de la comunidad gamer.",
        date="15/06/2025",
        idJournalist=1
    ),
    Article(
        id=2,
        title="Mapher Game lanza su nuevo título",
        body="El estudio sevillano Mapher Game sorprende con un juego de puzles espaciales que ya acumula miles de descargas.",
        date="20/06/2025",
        idJournalist=2
    ),
    Article(
        id=3,
        title="La industria española del gaming en crecimiento",
        body="España se consolida como un referente en el desarrollo de videojuegos con estudios que apuestan por la creatividad y la tecnología.",
        date="25/06/2025",
        idJournalist=3
    )
]

app = FastAPI()

@app.get("/articles")
def get_articles():
    return article_list

@app.get("/articles/id/{id_articles}")
def get_articles_id(id_articles: int):
    articles = [article for article in article_list if article.id == id_articles]
    return articles[0] if articles else {"error": "Article not found"}

@app.get("/articles/title/{title_articles}")
def get_article_by_title(title_articles: str):
    articles = [article for article in article_list if article.title == title_articles]
    return articles[0] if articles else {"error": "Article not found"}

@app.get("/articles/date/{date_articles}")
def get_article_by_date(date_articles: str):
    articles = [article for article in article_list if article.date == date_articles]
    return articles if articles else {"error": "Articles not found"}

@app.post("/article", status_code=201)
def add_article(articles: Article):
    articles.id = next_id()
    article_list.append(articles)
    return articles

@app.put("/article/{id}", response_model=Article)
def modify_article(id: int, article: Article):
    for index, saved_user in enumerate(article_list):
        if saved_user.id == id:
            article.id = id
            article_list[index] = article
            return article
    
    raise HTTPException(status_code=404, detail="Article not found")

@app.delete("/article/{id}")
def delete_article(id:int):
    for saved_article in article_list:
        if saved_article.id == id:
            article_list.remove(saved_article)
            return {}
    raise HTTPException(status_code=404, detail="Article not found")

def next_id():
    return (max(article_list, key=lambda x: x.id).id + 1) if article_list else 1
