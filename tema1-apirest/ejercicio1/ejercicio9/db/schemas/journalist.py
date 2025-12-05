# db/schemas/journalist.py

def journalist_schema(journalist) -> dict:
    return {
        "id": str(journalist["_id"]), # Convertimos el ObjectId de Mongo a String
        "dni": journalist["dni"],
        "name": journalist["name"],
        "surname": journalist["surname"],
        "telephone": journalist["telephone"], # Corregido (antes tenías age)
        "specialty": journalist["specialty"]  # Agregado
    }

def journalists_schema(journalists) -> list:
    return [journalist_schema(journalist) for journalist in journalists]