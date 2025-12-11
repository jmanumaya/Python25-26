from typing import Optional
from pydantic import BaseModel

# Entidad Client
class Client(BaseModel):
    id: Optional[str] = None
    name: str
    age: int
    weight: float
    goal: str  # Perder peso, Ganar músculo, etc.
    id_trainer: str