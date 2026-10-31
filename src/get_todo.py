from utils import table, response


def handler(event, context):
    todo_id = event.get("pathParameters", {}).get("id")

    if not todo_id:
        return response(400, {"message": "Falta el ID de la tarea"})

    result = table.get_item(Key={"id": todo_id})
    todo = result.get("Item")

    if not todo:
        return response(404, {"message": "Tarea no encontrada"})

    return response(200, todo)
