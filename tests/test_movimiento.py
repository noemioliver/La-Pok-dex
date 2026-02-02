from movimientos import Movimiento

def test_crear_movimiento():
    movimiento = Movimiento("Placaje", 10)

    assert movimiento.nombre == "Placaje"
    assert movimiento.poder == 10
