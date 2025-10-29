from fastapi import FastAPI
from router import journalist, article
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(journalist.router)
app.include_router(article.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")   
def inicio():
    return {"message": "Welcome to the News API"}