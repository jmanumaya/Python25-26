# db/schemas/alumno.py

def alumno_schema(alumno) -> dict:
    return {
        "id": str(alumno["_id"]),
        "nombre": alumno["nombre"],
        "apellidos": alumno["apellidos"],
        "fecha_nacimiento": alumno["fecha_nacimiento"],
        "curso": alumno["curso"],
        "repetidor": alumno["repetidor"],
        "id_colegio": alumno["curso"],
    }

def alumnos_schema(alumnos) -> list:
    return [alumno_schema(alumno) for alumno in alumnos]