from typing import Optional
from pydantic import BaseModel

class Album(BaseModel):
    id: Optional [str] = None
    title: str
    release_year: int
    sales: int
    id_band: str