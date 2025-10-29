from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/web_pages", tags=["Web Pages"])

class Web_pages(BaseModel):
    id:int
    title:str
    theme:str
    url:str
    id_programmer:int

list_web_pages = [
    Web_pages(id=1, title="Joyago Games", theme="Personal", url="https://joyagogames.com", id_programmer=1),
    Web_pages(id=2, title="Blog de Tecnología", theme="Blog", url="https://tecnoblog.com", id_programmer=2),
    Web_pages(id=3, title="Tienda GamerZone", theme="E-commerce", url="https://gamerzone.store", id_programmer=3),
    Web_pages(id=4, title="Noticias Futboleras", theme="Deportes", url="https://futbolnews.es", id_programmer=4),
    Web_pages(id=5, title="Foro de Programadores", theme="Comunidad", url="https://devforum.net", id_programmer=5),
]

# ----------- FUNCIONES AUXILIARES ------------
def next_id():
    return (max(list_web_pages, key=lambda x: x.id).id + 1) if list_web_pages else 1

def find_journalist_by_id(id: int):
    return next((wp for wp in list_web_pages if wp.id == id), None)

# ----------- ENDPOINTS ------------

router.get("/", response_model=list[Web_pages])
def get_webpages():
    return list_web_pages