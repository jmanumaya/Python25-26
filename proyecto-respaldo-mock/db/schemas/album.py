# db/schemas/album.py

def album_schema(album) -> dict:
    return {
        "id": str(album["_id"]),
        "title": album["title"],
        "release_year": album["release_year"],
        "sales": album["sales"],
        "id_band": album["id_band"] 
    }

def albums_schema(albums) -> list:
    return [album_schema(album) for album in albums]