from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

libros = []

@app.get("/")
def index():
    return {"message": "Hola Profe"}

@app.get("/Libros/{id}", response_model=Libro)
def mostrar_libro(id: int):
    for libro in libros:
        if libro.id == id:
            return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")

@app.post("/Libros", response_model=Libro)
def insertar_libro(libro: Libro):
    libros.append(libro)
    return {"message": f"libro {libro.titulo} insertado"}

@app.get("/Libros", response_model=List[Libro])
def obtener_libros():
    return libros
