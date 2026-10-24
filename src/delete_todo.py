from utils import table, response


def lambda_handler(event, context):
    todo_id = event.get("pathParameters", {}).get("id")

    if not todo_id:
        return response(400, {"message": "Falta el ID de la tarea"})

    try:
        result = table.delete_item(
            Key={"id": todo_id},
            ConditionExpression="attribute_exists(id)",
            ReturnValues="ALL_OLD",
        )
        return response(200, {
            "message": "Tarea eliminada",
            "todo": result["Attributes"],
        })
    except table.meta.client.exceptions.ConditionalCheckFailedException:
        return response(404, {"message": "Tarea no encontrada"})
