from fastapi import FastAPI
from routers import trainers, clients, auth_users

app = FastAPI(
    title="Gym API",
    description="API para gestión de entrenadores y clientes de gimnasio",
    version="1.0.0"
)

# Routers
app.include_router(auth_users.router)
app.include_router(trainers.router)
app.include_router(clients.router)

@app.get("/")
def root():
    return {
        "message": "Gym API",
        "endpoints": {
            "register": "/register",
            "login": "/login",
            "trainers": "/trainers",
            "clients": "/clients",
            "docs": "/docs"
        }
    }