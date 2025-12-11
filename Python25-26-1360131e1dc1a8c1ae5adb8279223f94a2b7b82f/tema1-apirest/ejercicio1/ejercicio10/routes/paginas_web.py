from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/web_pages", tags=["Web Pages"])

class Web_page(BaseModel):
    id: int
    title: str
    theme: str
    url: str
    id_programmer: int

list_web_pages = [
    Web_page(id=1, title="Joyago Games", theme="Personal", url="https://joyagogames.com", id_programmer=1),
    Web_page(id=2, title="Blog de Tecnología", theme="Blog", url="https://tecnoblog.com", id_programmer=2),
    Web_page(id=3, title="Tienda GamerZone", theme="E-commerce", url="https://gamerzone.store", id_programmer=3),
    Web_page(id=4, title="Noticias Futboleras", theme="Deportes", url="https://futbolnews.es", id_programmer=4),
    Web_page(id=5, title="Foro de Programadores", theme="Comunidad", url="https://devforum.net", id_programmer=5),
]

# ----------- FUNCIONES AUXILIARES ------------
def next_id():
    return (max(list_web_pages, key=lambda x: x.id).id + 1) if list_web_pages else 1

def find_web_page_by_id(id: int):
    return next((wp for wp in list_web_pages if wp.id == id), None)

# ----------- ENDPOINTS ------------

@router.get("/", response_model=list[Web_page])
def get_webpages():
    return list_web_pages

@router.get("/{id}", response_model=Web_page)
def get_web_page_by_id(id: int):
    web_page = find_web_page_by_id(id)
    if not web_page:
        raise HTTPException(status_code=404, detail="Web Page not found.")
    return web_page

@router.get("/title/{title}", response_model=Web_page)
def get_web_page_by_title(title: str):
    web_page = next((wp for wp in list_web_pages if wp.title.lower() == title.lower()), None)
    if not web_page:
        raise HTTPException(status_code=404, detail="Web Page not found.")
    return web_page

@router.get("/programmer/{id_programmer}", response_model=list[Web_page])
def get_web_pages_by_programmer(id_programmer: int):
    pages = [wp for wp in list_web_pages if wp.id_programmer == id_programmer]
    if not pages:
        raise HTTPException(status_code=404, detail="No web pages found for this programmer.")
    return pages

@router.post("", response_model=Web_page, status_code=201)
def add_web_page(web_page: Web_page):
    web_page.id = next_id()
    list_web_pages.append(web_page)
    return web_page

@router.put("/{id}", response_model=Web_page)
def modify_web_page(id: int, web_page: Web_page):
    for index, saved_web_page in enumerate(list_web_pages):
        if saved_web_page.id == id:
            web_page.id = id
            list_web_pages[index] = web_page
            return web_page
    raise HTTPException(status_code=404, detail="Web Page not found.")

@router.delete("/{id}", status_code=204)
def delete_web_page(id: int):
    web_page = find_web_page_by_id(id)
    if not web_page:
        raise HTTPException(status_code=404, detail="Web Page not found.")
    list_web_pages.remove(web_page)
    return