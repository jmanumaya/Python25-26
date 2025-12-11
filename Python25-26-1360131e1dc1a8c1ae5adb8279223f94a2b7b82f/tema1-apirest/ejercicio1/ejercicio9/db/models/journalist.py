from typing import Optional
from pydantic import BaseModel

class Journalist(BaseModel):
    id: Optional [str] = None
    dni: str
    name: str
    surname: str
    telephone: int
    specialty: str