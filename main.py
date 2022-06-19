# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, Query
from fastapi import Body, Query


app = FastAPI()

# Models
class Person(BaseModel):
    # Nombre | Tipo
    first_name: str
    last_name: str
    age: int
    # Estos campos son opcionales, pueden ser enviados o no en el Request Body
    hair_color: Optional[str] = None
    is_married: Optional[bool] = False


@app.get("/")
def home():
    return  {"Hello": "World"}

# Request and Response body
@app.post("/person/new")
# Tipo de parametro Body
# Cuando tiene "..." significa que es obligatorio, en éste caso en el Body
def create_person(person: Person = Body(...)):
    return person


# Validaciones: Query parameters

@app.get("/person/detail")
def show_person(
    # Los Query parameters deberian ser siempre opcionales
    # En este caso, por ejemplo, se espera un tipo str y el valor por default 
    # en caso de no ingresar nada será None 
    name: Optional[str] = Query(None, max_length=50),
    # En este caso, cómo ejemplo, hacemos que age sea obligatorio con los puntos
    age: Optional[int] = Query(...)
):
    return {name: age} 