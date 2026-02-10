from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola mundo"}

@app.get("/pokemon/{id}")
def obtener_pokemon(id: int):
    return {"id": id, "nombre": "pokemon molón"}

@app.post("/pokemon")
def crear_pokemon():
    return {"status": "pokemon creado"}

@app.put("/pokemon/{id}")
def actualizar_pokemon(id: int):
    return {"status": "pokemon actualizado", "id": id}

@app.delete("/pokemon/{id}")
def eliminar_pokemon(id: int):
    return {"status": "pokemon eliminado", "id": id}
