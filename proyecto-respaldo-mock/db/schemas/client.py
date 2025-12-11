def client_schema(client) -> dict:
    # El id en base de datos es _id
    return {
        "id": str(client["_id"]),
        "name": client["name"],
        "age": client["age"],
        "weight": client["weight"],
        "goal": client["goal"],
        "id_trainer": client["id_trainer"]
    }


def clients_schema(clients) -> list:
    return [client_schema(client) for client in clients]