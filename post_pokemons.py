import requests
import json

# JSON de los 20 pokemons
pokemons = [
    {
        "id": 1,
        "nombre": "Pikachu",
        "tipo": "Electrico",
        "nivel": 15,
        "vida": 120,
        "fuerza": 18,
        "defensa": 10,
        "velocidad": 90,
        "movimientos": ["Impactrueno", "Placaje", "Rayo", "Ataque rapido"]
    },
    {
        "id": 2,
        "nombre": "Charmander",
        "tipo": "Fuego",
        "nivel": 12,
        "vida": 100,
        "fuerza": 20,
        "defensa": 12,
        "velocidad": 80,
        "movimientos": ["Lanzallamas", "Arañazo", "Ascuas", "Cola Férrea"]
    },
    {
        "id": 3,
        "nombre": "Bulbasaur",
        "tipo": "Planta",
        "nivel": 14,
        "vida": 110,
        "fuerza": 16,
        "defensa": 14,
        "velocidad": 60,
        "movimientos": ["Látigo Cepa", "Placaje", "Hoja Afilada", "Drenadoras"]
    },
    {
        "id": 4,
        "nombre": "Squirtle",
        "tipo": "Agua",
        "nivel": 13,
        "vida": 115,
        "fuerza": 17,
        "defensa": 15,
        "velocidad": 65,
        "movimientos": ["Pistola Agua", "Caparazonazo", "Placaje", "Rugido"]
    },
    {
        "id": 5,
        "nombre": "Jigglypuff",
        "tipo": "Normal",
        "nivel": 10,
        "vida": 130,
        "fuerza": 12,
        "defensa": 10,
        "velocidad": 50,
        "movimientos": ["Canto", "Placaje", "Encanto", "Dulce Kilo"]
    },
    {
        "id": 6,
        "nombre": "Meowth",
        "tipo": "Normal",
        "nivel": 11,
        "vida": 105,
        "fuerza": 14,
        "defensa": 10,
        "velocidad": 70,
        "movimientos": ["Arañazo", "Placaje", "Ladrido", "Bofeton"]
    },
    {
        "id": 7,
        "nombre": "Psyduck",
        "tipo": "Agua",
        "nivel": 12,
        "vida": 110,
        "fuerza": 15,
        "defensa": 12,
        "velocidad": 55,
        "movimientos": ["Confusion", "Pistola Agua", "Golpe Cabeza", "Reflejo"]
    },
    {
        "id": 8,
        "nombre": "Machop",
        "tipo": "Lucha",
        "nivel": 14,
        "vida": 120,
        "fuerza": 18,
        "defensa": 14,
        "velocidad": 60,
        "movimientos": ["Puño Fuego", "Golpe Karate", "Placaje", "Patada Baja"]
    },
    {
        "id": 9,
        "nombre": "Geodude",
        "tipo": "Roca",
        "nivel": 13,
        "vida": 130,
        "fuerza": 20,
        "defensa": 18,
        "velocidad": 40,
        "movimientos": ["Roca Afilada", "Placaje", "Rodar", "Terremoto"]
    },
    {
        "id": 10,
        "nombre": "Vulpix",
        "tipo": "Fuego",
        "nivel": 12,
        "vida": 95,
        "fuerza": 16,
        "defensa": 12,
        "velocidad": 65,
        "movimientos": ["Lanzallamas", "Cola Férrea", "Arañazo", "Ascuas"]
    },
    {
        "id": 11,
        "nombre": "Eevee",
        "tipo": "Normal",
        "nivel": 15,
        "vida": 105,
        "fuerza": 17,
        "defensa": 12,
        "velocidad": 75,
        "movimientos": ["Placaje", "Encanto", "Mordisco", "Rapidez"]
    },
    {
        "id": 12,
        "nombre": "Snorlax",
        "tipo": "Normal",
        "nivel": 20,
        "vida": 250,
        "fuerza": 20,
        "defensa": 18,
        "velocidad": 30,
        "movimientos": ["Placaje", "Descanso", "Mordisco", "Golpe Cuerpo"]
    },
    {
        "id": 13,
        "nombre": "Gengar",
        "tipo": "Fantasma",
        "nivel": 18,
        "vida": 120,
        "fuerza": 19,
        "defensa": 12,
        "velocidad": 95,
        "movimientos": ["Bola Sombra", "Hipnosis", "Confusion", "Lengüetazo"]
    },
    {
        "id": 14,
        "nombre": "Alakazam",
        "tipo": "Psíquico",
        "nivel": 17,
        "vida": 110,
        "fuerza": 18,
        "defensa": 12,
        "velocidad": 120,
        "movimientos": ["Confusion", "Psíquico", "Rayo", "Telekinesis"]
    },
    {
        "id": 15,
        "nombre": "Onix",
        "tipo": "Roca",
        "nivel": 16,
        "vida": 150,
        "fuerza": 15,
        "defensa": 18,
        "velocidad": 70,
        "movimientos": ["Roca Afilada", "Rodar", "Terremoto", "Placaje"]
    },
    {
        "id": 16,
        "nombre": "Vaporeon",
        "tipo": "Agua",
        "nivel": 16,
        "vida": 130,
        "fuerza": 17,
        "defensa": 14,
        "velocidad": 80,
        "movimientos": ["Pistola Agua", "Hidrobomba", "Placaje", "Rugido"]
    },
    {
        "id": 17,
        "nombre": "Flareon",
        "tipo": "Fuego",
        "nivel": 16,
        "vida": 120,
        "fuerza": 19,
        "defensa": 12,
        "velocidad": 85,
        "movimientos": ["Lanzallamas", "Ascuas", "Placaje", "Mordisco"]
    },
    {
        "id": 18,
        "nombre": "Jolteon",
        "tipo": "Electrico",
        "nivel": 16,
        "vida": 115,
        "fuerza": 17,
        "defensa": 10,
        "velocidad": 110,
        "movimientos": ["Impactrueno", "Placaje", "Rayo", "Ataque Rapido"]
    },
    {
        "id": 19,
        "nombre": "Dragonite",
        "tipo": "Dragon",
        "nivel": 20,
        "vida": 200,
        "fuerza": 20,
        "defensa": 16,
        "velocidad": 100,
        "movimientos": ["Garra Dragon", "Puño Dragon", "Vuelo", "Cola Dragon"]
    },
    {
        "id": 20,
        "nombre": "Mewtwo",
        "tipo": "Psíquico",
        "nivel": 25,
        "vida": 180,
        "fuerza": 20,
        "defensa": 15,
        "velocidad": 120,
        "movimientos": ["Psíquico", "Confusion", "Maldicion", "Rayo"]
    }
]

# URL de tu API
url = "http://127.0.0.1:8000/pokemon"

# Recorrer el JSON y hacer POST a la API
for p in pokemons:
    response = requests.post(url, json=p)
    if response.status_code == 200:
        print(f"✅ Pokémon {p['nombre']} creado correctamente")
    else:
        print(f"❌ Error al crear {p['nombre']}: {response.status_code}, {response.text}")
