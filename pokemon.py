# Clase pokemon

## Atributos
# - Nombre
# - Tipo
# - Nivel
# - Vida (Inicial 100-300)
# - Fuerza (Maz 20)
# - Defensa (Max 18)
# - Velocidad (Max 100)
# - movimientos[4] - Solo nombre

## Metodos
# ejecutar_movimiento(self, otro_pokemon) 
# Se decide aleatoriamente entre los 4 movimientos disponibles en el pokemon
# Lanza este movimiento
# se calcula el daño y se ejecuta la funciñon recibir dano del otro pokemon
# daño = self.ataque - otro_pokemon.defensa


# recibir_dano()
# Se resta a la vida actual el daño recibido

class Pokemon:
    def __init__(self, nombre, tipo, movimientos):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = 10
        self.fuerza = 20
        self.defensa = 18
        self.velocidad = 100
        self.movimientos = movimientos

def ejecutar_movimiento(self, otro_pokemon):
    movimiento = self.movimientos[0]
    print(self.nombre, "usa", movimiento)
    dano = self.fuerza - otro_pokemon.defensa
    if dano < 0:
         dano = 0

def recibir_dano(self, dano):
        self.vida = self.vida - dano
        print(self.nombre, "tiene", self.vida, "de vida")