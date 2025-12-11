def trainer_schema(trainer) -> dict:
    # El id en base de datos es _id
    return {
        "id": str(trainer["_id"]),
        "name": trainer["name"],
        "specialty": trainer["specialty"],
        "shift": trainer["shift"]
    }


def trainers_schema(trainers) -> list:
    return [trainer_schema(trainer) for trainer in trainers]