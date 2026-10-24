from utils import table, response, parse_body


def lambda_handler(event, context):
    todo_id = event.get("pathParameters", {}).get("id")

    if not todo_id:
        return response(400, {"message": "Falta el ID de la tarea"})

    body = parse_body(event)
    if body is None:
        return response(400, {"message": "JSON inválido"})

    updates = {}
    if "title" in body:
        if not isinstance(body["title"], str) or not body["title"].strip():
            return response(400, {"message": "El título no puede estar vacío"})
        updates["title"] = body["title"]

    if "completed" in body:
        if not isinstance(body["completed"], bool):
            return response(400, {"message": "completed debe ser true o false"})
        updates["completed"] = body["completed"]

    if not updates:
        return response(400, {"message": "No hay campos para actualizar"})

    names = {}
    values = {}
    expressions = []

    for key, value in updates.items():
        names[f"#{key}"] = key
        values[f":{key}"] = value
        expressions.append(f"#{key} = :{key}")

    try:
        result = table.update_item(
            Key={"id": todo_id},
            UpdateExpression="SET " + ", ".join(expressions),
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ConditionExpression="attribute_exists(id)",
            ReturnValues="ALL_NEW",
        )
        return response(200, result["Attributes"])
    except table.meta.client.exceptions.ConditionalCheckFailedException:
        return response(404, {"message": "Tarea no encontrada"})
