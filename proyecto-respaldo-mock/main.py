from fastapi import FastAPI
from router import auth_users, band, album

app = FastAPI()

# Routers
app.include_router(band.router)
app.include_router(album.router)
app.include_router(auth_users.router)

@app.get("/")   
def inicio():
    return {"message": "Welcome to the News API"}