from utils import table, response


def lambda_handler(event, context):
    result = table.scan()
    todos = result.get("Items", [])

    while "LastEvaluatedKey" in result:
        result = table.scan(ExclusiveStartKey=result["LastEvaluatedKey"])
        todos.extend(result.get("Items", []))

    return response(200, todos)
