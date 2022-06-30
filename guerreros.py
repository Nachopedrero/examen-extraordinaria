from enum import Enum


class Guerrero:
    def __init__(self, defensa, daño, vida):
        try:
            if daño > 50 or daño < 0 or defensa > 100 or defensa < 40 or vida > 100 or vida < 70:
                raise Exception("error en los datos de daño y defensa")
        except Exception as error:
            print(error)
        self._defensa = defensa
        self._daño = daño

        self.vida = vida

    def is_vivo(self):
        if vida > 0:
            return True
        Print("a su heroe le quedan " + vida + " puntoss de vida ")

    def get_vida(self):
        return self._vida

    def get_arma(self):
        return self._arma

    def get_guerrero(self):
        return self._guerrero

    def get_defensa(self):
        return self._defensa

    def is_alive(self):
        if self._vida > 0:
            return True
        else:
            return False

    def fight_defense(self, points_of_damage):
        daño = points_of_damage - self._defensa
        self._vida = self._vida - daño
        return


class Boxeador(Guerrero):
    def __init__(self, defensa, daño, vida):
        self.defensa = super(defensa) - 10
        self.daño = super(daño) + 10
        super.__init__(vida)

    def get_vida(self):
        return self._vida

    def get_arma(self):
        return self._arma

    def get_guerrero(self):
        return self._guerrero

    def get_defensa(self):
        return self._defensa

    def is_alive(self):
        if self._vida > 0:
            return True
        else:
            return False

    def fight_defense(self, points_of_damage):
        daño = points_of_damage - self._defensa
        self._vida = self._vida - daño
        return

    def is_vivo(self):
        if vida > 0:
            return True
        Print("a su heroe le quedan " + vida + " puntoss de vida ")


class Mago(Guerrero):
    def __init__(self, defensa, daño, vida):
        self.defensa = super(defensa) - 14
        self.vida = super(vida) + 10
        super.__init__(daño)

    def get_vida(self):
        return self._vida

    def get_arma(self):
        return self._arma

    def get_guerrero(self):
        return self._guerrero

    def get_defensa(self):
        return self._defensa

    def is_vivo(self):
        if vida > 0:
            return True
        Print("a su heroe le quedan " + vida + " puntoss de vida ")

    def is_alive(self):
        if self._vida > 0:
            return True
        else:
            return False

    def fight_defense(self, points_of_damage):
        daño = points_of_damage - self._defensa
        self._vida = self._vida - daño
        return


warrior1 = Guerrero(50, 76, 67)