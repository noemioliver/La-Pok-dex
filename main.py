# Script que me va a ejecutar la logica siguiente:

# Escenario
# Definir que pokemons van a combatir (2 -> p1 y p2)
# Definir quien inicia el ataque: el que tenga más velocidad
# Logica de turno: 
# - 1 accion por turno para cada pokemon
# - ataca 1 pokemon el 2 recibe daño en función del p1.ataque - p2.defensa
# - ataca 2 pokemon el 1 recibe daño en función del p2.ataque - p1.defensa

# condiciones victoria o derrota
# El primer pokemon que se queda a vvida <= 0 pierde<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

from pokemon import Pokemon
from combate import Combate
from movimientos import Movimiento

placaje = Movimiento("Placaje", 10)
encanto = Movimiento("Encanto", 5)
mordisco = Movimiento("Mordisco", 12)
rapidez = Movimiento("Rapidez", 15)

lanzallamas = Movimiento("Lanzallamas", 20)
cola_ferrea = Movimiento("Cola Férrea", 18)
aranazo = Movimiento("Arañazo", 8)
ascuas = Movimiento("Ascuas", 12)


p1 = Pokemon(
    "Eevee",
    "Normal",
    vida = 55,
    fuerza = 55,
    defensa = 50,
    velocidad = 55,
    movimientos=[placaje, encanto, mordisco, rapidez]
)

p2 = Pokemon(
    nombre = "Vulpix",
    tipo = "Fuego",
    vida = 38,
    fuerza = 41,
    defensa = 40,
    velocidad = 65,
    movimientos = [lanzallamas, cola_ferrea, aranazo, ascuas]
)


batalla = Combate(p1, p2)
batalla.iniciar()