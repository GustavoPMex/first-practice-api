# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field

# FastAPI
from fastapi import FastAPI, Query
from fastapi import Body, Query, Path


app = FastAPI()

# Models

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

# Creamos un nuevo modelo
class Location(BaseModel):
    # Nombre | tipo
    city: str
    state: str
    country: str

class Person(BaseModel):
    # Nombre | Tipo
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    # Estos campos son opcionales, pueden ser enviados o no en el Request Body
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)


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
    name: Optional[str] = Query(
        None,
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters"
    ),
    # En este caso, cómo ejemplo, hacemos que age sea obligatorio con los puntos
    age: Optional[int] = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required"
    )
):
    return {name: age} 

# Validaciones: Path parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        # Mayor a 0 (gt = Greater than)
        gt=0,
        title="Person Id",
        description="This is the person Id"
    )
):
    return {person_id: "It exists"}

# Validaciones: Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())

    return results