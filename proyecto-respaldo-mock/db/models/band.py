from typing import Optional
from pydantic import BaseModel

class Band(BaseModel):
    id: Optional [str] = None
    name: str
    genre: str
    start_year: int