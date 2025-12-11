# db/schemas/journalist.py

def journalist_schema(journalist) -> dict:
    return {
        "id": str(journalist["_id"]),
        "dni": journalist["dni"],
        "name": journalist["name"],
        "surname": journalist["surname"],
        "telephone": journalist["telephone"],
        "specialty": journalist["specialty"]
    }

def journalists_schema(journalists) -> list:
    return [journalist_schema(journalist) for journalist in journalists]