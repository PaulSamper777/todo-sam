import json
import uuid
from datetime import datetime, timezone

from utils import table, response, parse_body


def lambda_handler(event, context):
    body = parse_body(event)
    if body is None:
        return response(400, {"message": "JSON inválido"})

    title = body.get("title")
    if not title or not isinstance(title, str):
        return response(400, {"message": "El campo 'title' es obligatorio"})

    todo = {
        "id": str(uuid.uuid4()),
        "title": title,
        "completed": bool(body.get("completed", False)),
        "createdAt": datetime.now(timezone.utc).isoformat(),
    }

    table.put_item(Item=todo)
    return response(201, todo)
