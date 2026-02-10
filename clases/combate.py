class Combate:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def iniciar(self):
        print("¡Comienza el combate entre", self.pokemon1.nombre, "y", self.pokemon2.nombre, "!")

        while self.pokemon1.vida > 0 and self.pokemon2.vida > 0:
            if self.pokemon1.velocidad >= self.pokemon2.velocidad:
                if self.pokemon1.vida > 0:
                    self.atacar(self.pokemon1, self.pokemon2)
                if self.pokemon2.vida > 0:
                    self.atacar(self.pokemon2, self.pokemon1)
            else:
                if self.pokemon2.vida > 0:
                    self.atacar(self.pokemon2, self.pokemon1)
                if self.pokemon1.vida > 0:
                    self.atacar(self.pokemon1, self.pokemon2)

        if self.pokemon1.vida > 0:
            print("¡" + self.pokemon1.nombre + " gana el combate!")
        else:
            print("¡" + self.pokemon2.nombre + " gana el combate!")

    def atacar(self, atacante, defensor):
        movimiento = atacante.movimientos[0]  
        print(atacante.nombre, "usa", movimiento.nombre)

        dano = atacante.fuerza + movimiento.poder - defensor.defensa
        if dano < 0:
            dano = 0

        defensor.vida -= dano
        if defensor.vida < 0:
            defensor.vida = 0

        print(defensor.nombre, "tiene", defensor.vida, "de vida")
