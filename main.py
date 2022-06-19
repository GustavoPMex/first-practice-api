# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body


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