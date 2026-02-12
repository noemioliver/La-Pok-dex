from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


pokemones = {}

class Movimiento(BaseModel):
    nombre: str
    poder: int


class Pokemon(BaseModel):
    nombre: str
    tipo: str
    vida: int
    fuerza: int
    defensa: int
    velocidad: int
    movimientos: list[Movimiento]


class PokemonCreateModel(BaseModel):
    nombre: str
    tipo: str
    vida: int
    fuerza: int
    defensa: int
    velocidad: int
    movimientos: list[str]
@app.post("/pokemon")
def crear_pokemon(id: int, pokemon_data: PokemonCreateModel):
    movimientos = [Movimiento(nombre=m, poder=10) for m in pokemon_data.movimientos]
    nuevo_pokemon = Pokemon(
        nombre=pokemon_data.nombre,
        tipo=pokemon_data.tipo,
        vida=pokemon_data.vida,
        fuerza=pokemon_data.fuerza,
        defensa=pokemon_data.defensa,
        velocidad=pokemon_data.velocidad,
        movimientos=movimientos
    )
    pokemones[id] = nuevo_pokemon


    return {
        "status": "Pokemon creado con éxito 💛",
        "id": id,
        "pokemon": {
            "nombre": nuevo_pokemon.nombre,
            "tipo": nuevo_pokemon.tipo,
            "vida": nuevo_pokemon.vida,
            "fuerza": nuevo_pokemon.fuerza,
            "defensa": nuevo_pokemon.defensa,
            "velocidad": nuevo_pokemon.velocidad,
            "movimientos": [m.nombre for m in nuevo_pokemon.movimientos]
        }
    }

@app.get("/")
def root():
    return {"message": "Hola mundo"}

@app.get("/pokemon/{id}")
def obtener_pokemon(id: int):
    return {"id": id, "nombre": "pokemon molón"}

'''@app.post("/pokemon")
def crear_pokemon():
    return {"status": "pokemon creado"}'''

@app.put("/pokemon/{id}")
def actualizar_pokemon(id: int):
    return {"status": "pokemon actualizado", "id": id}

@app.delete("/pokemon/{id}")
def eliminar_pokemon(id: int):
    return {"status": "pokemon eliminado", "id": id}

