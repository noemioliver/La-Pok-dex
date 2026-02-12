# clases/models.py
from pydantic import BaseModel
from typing import List

class PokemonCreateModel(BaseModel):
    nombre: str
    tipo: str
    nivel: int
    vida: int
    fuerza: int
    defensa: int
    velocidad: int
    movimientos: List[str]  
