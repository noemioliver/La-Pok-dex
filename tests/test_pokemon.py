from pokemon import Pokemon
from movimientos import Movimiento


def test_recibir_dano_baja_vida():
    pokemon = Pokemon("Eevee", "Normal", 50, 10, 5, 5, [])
    pokemon.recibir_dano(10)

    assert pokemon.vida == 40

