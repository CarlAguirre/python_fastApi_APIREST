

from email.policy import HTTP
from operator import index
from operator import index
from typing import Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Definición de la aplicación FastAPI
app = FastAPI()

# Definición del modelo de datos
class Curso(BaseModel):
    id: Optional[str] = None
    nombre: str
    descripcion: Optional[str] = None
    nivel: str
    duracion: int  # duración en horas


# Simulación de una base de datos en memoria
cursos_db = []

#CRUD

# Get all cursos
@app.get("/cursos/", response_model=list[Curso])
def obtener_cursos():
    return cursos_db

# get curso por id
@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id: str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None) # next para obtener el primer elemento que cumple la condición
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso

# Create curso
@app.post("/cursos/", response_model=Curso)
def crear_curso(curso: Curso):
    curso.id = str(uuid.uuid4())  # uuid para generar un ID único
    cursos_db.append(curso)
    return curso

# Actuyalizar curso
@app.put("/cursos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id: str, curso_actualizado: Curso):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None) # next para obtener el primer elemento que cumple la condición
    
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    curso_actualizado.id = curso.id  # Mantener el mismo ID
    index = cursos_db.index(curso) # Obtener el índice del curso a actualizar  # noqa: F811
    cursos_db[index] = curso_actualizado
    return curso_actualizado

# Eliminar curso
@app.delete("/cursos/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id: str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None) # next para obtener el primer elemento que cumple la condición
    
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    cursos_db.remove(curso)
    return curso