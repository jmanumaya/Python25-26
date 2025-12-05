from typing import Optional
from pydantic import BaseModel

class Article(BaseModel):
    id: Optional [str] = None
    title: str
    body: str
    date: str
    idJournalist: str