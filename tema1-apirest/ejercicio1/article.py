from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator

app = FastAPI()

class Article(BaseModel):
    id: int | None = None
    title: str
    body: str
    date: str
    idJournalist: int

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


# ---------- FUNCIONES AUXILIARES ----------
def next_id():
    return (max(article_list, key=lambda x: x.id).id + 1) if article_list else 1

def find_article_by_id(id: int):
    return next((a for a in article_list if a.id == id), None)


# ---------- ENDPOINTS ----------
@app.get("/articles", response_model=list[Article])
def get_articles():
    return article_list


@app.get("/articles/{id_article}", response_model=Article)
def get_article_by_id(id_article: int):
    article = find_article_by_id(id_article)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@app.get("/articles/title/{title_article}", response_model=Article)
def get_article_by_title(title_article: str):
    article = next((a for a in article_list if a.title == title_article), None)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@app.get("/articles/date/{date_article}", response_model=list[Article])
def get_articles_by_date(date_article: str):
    articles = [a for a in article_list if a.date == date_article]
    if not articles:
        raise HTTPException(status_code=404, detail="No articles found for that date")
    return articles


@app.post("/articles", response_model=Article, status_code=201)
def add_article(article: Article):
    article.id = next_id()
    article_list.append(article)
    return article


@app.put("/articles/{id}", response_model=Article)
def modify_article(id: int, article: Article):
    for index, saved_article in enumerate(article_list):
        if saved_article.id == id:
            article.id = id
            article_list[index] = article
            return article
    raise HTTPException(status_code=404, detail="Article not found")


@app.delete("/articles/{id}", status_code=204)
def delete_article(id: int):
    article = find_article_by_id(id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    article_list.remove(article)
    return
