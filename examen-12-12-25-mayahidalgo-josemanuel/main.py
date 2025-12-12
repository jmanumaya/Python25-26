from fastapi import FastAPI
from routers import auth_users, colegios, alumnos

app = FastAPI()

# Routers
app.include_router(colegios.router)
app.include_router(alumnos.router)
app.include_router(auth_users.router)

@app.get("/")   
def inicio():
    return {"message": "Welcome to the News API"}