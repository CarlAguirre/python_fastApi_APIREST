# Backend FastAPI - API REST de Gestión de Cursos

API RESTful desarrollada con FastAPI para la gestión completa de cursos educativos. Implementa operaciones CRUD (Create, Read, Update, Delete) con validación de datos y documentación automática.

## 🚀 Características

- ✅ API REST completa con operaciones CRUD
- ✅ Validación automática de datos con Pydantic
- ✅ Documentación interactiva automática (Swagger UI)
- ✅ Identificadores únicos con UUID
- ✅ Respuestas con tipado fuerte
- ✅ Manejo de errores HTTP
- ✅ Hot-reload para desarrollo

## 📋 Requisitos

- Python 3.10+
- pip (gestor de paquetes de Python)

## 🔧 Instalación

1. **Clonar o descargar el proyecto**

2. **Crear un entorno virtual** (recomendado)
```bash
python3 -m venv .venv
source .venv/bin/activate  # En Linux/Mac
# .venv\Scripts\activate  # En Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## 🏃 Ejecución

Iniciar el servidor de desarrollo:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en: `http://127.0.0.1:8000`

## 📚 Documentación API

Una vez iniciado el servidor, accede a la documentación interactiva:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🛠️ Endpoints

### Obtener todos los cursos
```http
GET /cursos/
```

**Respuesta exitosa (200)**
```json
[
  {
    "id": "e442b622-2281-41d3-adaf-db228217d845",
    "nombre": "Python Avanzado",
    "descripcion": "Curso completo de Python",
    "nivel": "Avanzado",
    "duracion": 40
  }
]
```

### Obtener un curso por ID
```http
GET /cursos/{curso_id}
```

**Respuesta exitosa (200)**
```json
{
  "id": "e442b622-2281-41d3-adaf-db228217d845",
  "nombre": "Python Avanzado",
  "descripcion": "Curso completo de Python",
  "nivel": "Avanzado",
  "duracion": 40
}
```

**Error (404)** - Curso no encontrado

### Crear un nuevo curso
```http
POST /cursos/
```

**Body**
```json
{
  "nombre": "FastAPI desde Cero",
  "descripcion": "Aprende a crear APIs modernas",
  "nivel": "Intermedio",
  "duracion": 30
}
```

**Respuesta exitosa (200)**
```json
{
  "id": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "nombre": "FastAPI desde Cero",
  "descripcion": "Aprende a crear APIs modernas",
  "nivel": "Intermedio",
  "duracion": 30
}
```

### Actualizar un curso
```http
PUT /cursos/{curso_id}
```

**Body**
```json
{
  "nombre": "FastAPI Avanzado",
  "descripcion": "Curso actualizado",
  "nivel": "Avanzado",
  "duracion": 45
}
```

**Respuesta exitosa (200)** - Retorna el curso actualizado

**Error (404)** - Curso no encontrado

### Eliminar un curso
```http
DELETE /cursos/{curso_id}
```

**Respuesta exitosa (200)** - Retorna el curso eliminado

**Error (404)** - Curso no encontrado

## 📊 Modelo de Datos

### Curso

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| id | string | No* | UUID generado automáticamente |
| nombre | string | Sí | Nombre del curso |
| descripcion | string | No | Descripción detallada |
| nivel | string | Sí | Nivel del curso (Básico, Intermedio, Avanzado) |
| duracion | integer | Sí | Duración en horas |

*El ID se genera automáticamente al crear un curso

## 🧪 Ejemplos de Uso

### Usando cURL

**Crear un curso:**
```bash
curl -X POST "http://127.0.0.1:8000/cursos/" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Docker Fundamentals",
    "descripcion": "Aprende contenedores",
    "nivel": "Intermedio",
    "duracion": 20
  }'
```

**Obtener todos los cursos:**
```bash
curl -X GET "http://127.0.0.1:8000/cursos/"
```

**Actualizar un curso:**
```bash
curl -X PUT "http://127.0.0.1:8000/cursos/{curso_id}" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Docker Avanzado",
    "descripcion": "Contenedores y orquestación",
    "nivel": "Avanzado",
    "duracion": 35
  }'
```

**Eliminar un curso:**
```bash
curl -X DELETE "http://127.0.0.1:8000/cursos/{curso_id}"
```

### Usando Python (requests)

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# Crear curso
nuevo_curso = {
    "nombre": "Kubernetes Basics",
    "descripcion": "Orquestación de contenedores",
    "nivel": "Intermedio",
    "duracion": 25
}
response = requests.post(f"{BASE_URL}/cursos/", json=nuevo_curso)
curso = response.json()
print(f"Curso creado con ID: {curso['id']}")

# Obtener todos los cursos
response = requests.get(f"{BASE_URL}/cursos/")
cursos = response.json()
print(f"Total de cursos: {len(cursos)}")
```

## 🛠️ Tecnologías

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno y rápido
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Validación de datos
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI
- **Python 3.10+** - Lenguaje de programación

## 📝 Notas

- La base de datos actual es **en memoria**, los datos se pierden al reiniciar el servidor
- Para producción, considera integrar una base de datos persistente (PostgreSQL, MongoDB, etc.)
- Los IDs se generan automáticamente usando UUID4

## 🔮 Mejoras Futuras

- [ ] Integración con base de datos persistente (PostgreSQL/MongoDB)
- [ ] Autenticación y autorización (OAuth2/JWT)
- [ ] Paginación en listado de cursos
- [ ] Filtros y búsqueda avanzada
- [ ] Tests unitarios e integración
- [ ] Validación de niveles con Enum
- [ ] Rate limiting
- [ ] Logging avanzado

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

## 👤 Autor

Carlos A. Aguirre Lopez
Desarrollado como proyecto educativo de FastAPI.

---

**¡Disfruta construyendo APIs con FastAPI! 🚀**
