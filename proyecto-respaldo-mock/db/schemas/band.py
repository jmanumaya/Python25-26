# db/schemas/band.py

def band_schema(band) -> dict:
    return {
        "id": str(band["_id"]),
        "name": band["name"],
        "genre": band["genre"],
        "start_year": band["start_year"]
    }

def bands_schema(bands) -> list:
    return [band_schema(band) for band in bands]