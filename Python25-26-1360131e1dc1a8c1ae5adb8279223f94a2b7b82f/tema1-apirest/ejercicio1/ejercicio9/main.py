from fastapi import FastAPI
from router import journalist, article, auth_users, journalist_db, article_db
import os
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(journalist_db.router)
app.include_router(journalist.router)
app.include_router(article_db.router)
app.include_router(article.router)
app.include_router(auth_users.router)

if os.path.isdir("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def inicio():
    return {"message": "Welcome to the News API"}
