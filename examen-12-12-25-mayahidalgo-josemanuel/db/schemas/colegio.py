# db/schemas/colegio.py

def colegio_schema(colegio) -> dict:
    return {
        "id": str(colegio["_id"]), # Convertimos el ObjectId de Mongo a String
        "nombre": colegio["nombre"],
        "distrito": colegio["distrito"],
        "tipo": colegio["tipo"],
        "direccion": colegio["direccion"],
    }

def colegios_schema(colegios) -> list:
    return [colegio_schema(colegio) for colegio in colegios]