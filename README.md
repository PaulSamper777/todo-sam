# CRUD de TODOs con AWS SAM

Proyecto desarrollado como parte del workshop de implementación de una API REST para gestionar tareas (TODOs), utilizando AWS Lambda, Amazon API Gateway, Amazon DynamoDB y AWS SAM.

## Descripción del proyecto

La aplicación permite crear, consultar, actualizar y eliminar tareas mediante una API REST desplegada en AWS.

Cada tarea contiene los siguientes campos:

- `id`: identificador único de la tarea.
- `title`: título de la tarea.
- `completed`: indica si la tarea está completada.
- `createdAt`: fecha y hora de creación.

## Tecnologías utilizadas

- **AWS SAM:** construcción y despliegue de la aplicación serverless.
- **AWS Lambda:** ejecución de la lógica de negocio.
- **Amazon API Gateway:** exposición de los endpoints REST.
- **Amazon DynamoDB:** almacenamiento de las tareas.
- **Python:** implementación de las funciones Lambda.
- **Git y GitHub:** control de versiones y entrega del proyecto.

## Arquitectura

El flujo de la aplicación es:

1. El cliente realiza una petición HTTP.
2. Amazon API Gateway recibe la petición.
3. La función AWS Lambda correspondiente procesa la operación.
4. Amazon DynamoDB almacena, consulta, actualiza o elimina la tarea.
5. La API devuelve una respuesta HTTP al cliente.

## Estructura del proyecto

```text
todo-sam/
├── events/
│   └── create.json
├── src/
│   ├── create_todo.py
│   ├── delete_todo.py
│   ├── get_todo.py
│   ├── list_todos.py
│   ├── update_todo.py
│   ├── utils.py
│   └── requirements.txt
├── .gitignore
├── samconfig.toml
├── template.yaml
└── README.md
```

## API desplegada

**URL base:**

`https://9rro5xjola.execute-api.us-east-1.amazonaws.com/dev/todos`

**Región AWS:** `us-east-1`

### Endpoints CRUD

| Método HTTP | Endpoint | Descripción |
|---|---|---|
| POST | `/todos` | Crear una tarea |
| GET | `/todos` | Listar las tareas |
| GET | `/todos/{id}` | Consultar una tarea por su ID |
| PUT | `/todos/{id}` | Actualizar una tarea |
| DELETE | `/todos/{id}` | Eliminar una tarea |

### Ejemplos de uso

**Crear una tarea**

```bash
curl -i -X POST "$API" \
  -H "Content-Type: application/json" \
  -d '{"title":"Estudiar AWS SAM"}'
```

**Listar las tareas**

```bash
curl -i "$API"
```

**Consultar una tarea por ID**

```bash
curl -i "$API/$ID"
```

**Marcar una tarea como completada**

```bash
curl -i -X PUT "$API/$ID" \
  -H "Content-Type: application/json" \
  -d '{"completed":true}'
```

**Eliminar una tarea**

```bash
curl -i -X DELETE "$API/$ID"
```

Para ejecutar los ejemplos, define las variables en la terminal:

```bash
export API="https://9rro5xjola.execute-api.us-east-1.amazonaws.com/dev/todos"
export ID="ID_DE_LA_TAREA"
```

Sustituye `ID_DE_LA_TAREA` por el identificador real de una tarea.

## Despliegue con AWS SAM

Para construir el proyecto:

```bash
sam build
```

Para desplegar la aplicación:

```bash
sam deploy --guided
```

Durante la configuración, selecciona la región AWS correspondiente y el nombre del stack que utilizarás.

## Pruebas locales

El proyecto incluye un evento de ejemplo en `events/create.json`.

Para construir la aplicación:

```bash
sam build
```

Para invocar localmente la función de creación:

```bash
sam local invoke CreateTodoFunction \
  -e events/create.json \
  --env-vars env.json
```

El archivo `env.json` contiene la configuración local de variables de entorno y no se incluye en el repositorio.

## Monitoreo con CloudWatch

Los logs de la función Lambda se pueden consultar con:

```bash
sam logs -n CreateTodoFunction \
  --stack-name todo-sam-paul \
  --tail
```

Los registros permiten revisar las invocaciones, los tiempos de ejecución y el consumo de memoria de la función.

## Manejo de errores

La API contempla validaciones y respuestas de error, entre ellas:

- **400 Bad Request:** cuando faltan campos obligatorios o los datos enviados no cumplen las validaciones.
- **404 Not Found:** cuando se consulta o elimina una tarea que no existe.

## Evidencias del workshop

La carpeta `evidencias/` está destinada a almacenar las capturas de pantalla de las pruebas y del despliegue:

- Outputs de `sam deploy`.
- Creación de tareas (POST).
- Listado de tareas (GET).
- Consulta por ID (GET).
- Actualización de tareas (PUT).
- Eliminación de tareas (DELETE).
- Casos de error HTTP 400 y 404.
- Logs de una invocación en CloudWatch.

## Repositorio

GitHub: https://github.com/PaulSamper777/todo-sam

## Autor

**GitHub:** [PaulSamper777](https://github.com/PaulSamper777)

Proyecto realizado con fines educativos como parte del workshop CRUD de TODOs con AWS SAM.
