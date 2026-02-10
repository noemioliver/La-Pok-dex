
from clases.pokemon import Pokemon
from clases.movimientos import Movimiento
from clases.combate import Combate

def test_atacar_quita_vida():
    movimiento = Movimiento("Ataque", 5)

    p1 = Pokemon("A", "Normal", vida=10, fuerza=10, defensa=0, velocidad=1, movimientos=[movimiento])
    p2 = Pokemon("B", "Normal", vida=10, fuerza=5, defensa=0, velocidad=1, movimientos=[])

    combate = Combate(p1, p2)
    vida_inicial = p2.vida
    combate.atacar(p1, p2)
    assert p2.vida < vida_inicial

def test_iniciar_combate_termina():
   
    movimiento1 = Movimiento("Ataque", 5)
    movimiento2 = Movimiento("Golpe", 5)


    p1 = Pokemon("A", "Normal", vida=10, fuerza=10, defensa=0, velocidad=2, movimientos=[movimiento1])
    p2 = Pokemon("B", "Normal", vida=10, fuerza=5, defensa=0, velocidad=1, movimientos=[movimiento2])

    
    combate = Combate(p1, p2)
    combate.iniciar()
    assert p1.vida == 0 or p2.vida == 0
