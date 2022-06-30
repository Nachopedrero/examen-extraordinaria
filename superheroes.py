from enum import Enum
import random
from Escenarios import Escenarios
from SerVivo import SerVivo


class Superheroe_Type(Enum):
    def __init__(self,tipo,nombre):
        self.tipo = tipo
        self.nombre = nombre

    # usamos el metodo str que nos pasa los datos de la clase a modo de string
    def from_str(x):

        superheroe = x.upper()
        e = None

        for tp in Superheroe_Type:
            if superheroe == tp.name:
                e = tp
                break

        if type(e) != Superheroe_Type:
            raise TypeError("no es compatible con su tipo de superheroe")

        return e


class Movimiento_Type(Enum):
    ATAQUE = 1
    DEFENSA = 0


# creamos el constructor con algunas limitaciones para que los atributos de los ataques no sean injustos
class Movimientos:
    def __init__(self, nombre, tipo, daño):
        self._nombre = nombre
        self._tipo = tipo
        try:
            if daño < 0 or daño >= 100:
                raise Exception("error en el daño, datos incompatibes")

            self.daño = daño
        except Exception as error:
            print(error)

    def get_nombre(self):
        return self._nombre

    def get_tipo(self):
        return self._tipo

    def get_daño(self):
        return self._daño


class Superheroes(SerVivo):

    # creamos el constructor
    def __init__(self, alias, identidad, tipo, energia):
        self._identidad = identidad
        self._tipo = tipo
        try:
            if len(alias) >= 9 or alias.isalpha():
                raise Exception("ha habido un error en el alias")
            self.alias = alias
        except Exception as error:
            print(error)

        if type(tipo) != Superheroe_Type:
            raise TypeError("atributo incorrecto para tipo")
        if tipo.value:
            self._parrilla_poderes = [random.randint(3, 8), random.randint(1, 7), random.randint(2, 6),
                                      random.randint(2, 6), random.randint(1, 7), random.randint(1, 8)]
        else:
            self._parrilla_poderes = [random.randint(4, 7), random.randint(1, 8), random.randint(1, 8),
                                      random.randint(3, 8), random.randint(1, 8), random.randint(3, 7)]
        if type(esc) != Escenarios:
            raise TypeError("atributo incorrecto para tipo")

        self._coste = (esc.get_monedas() / esc.get_miembros_ekip()) * (sum(self._parrilla_poderes) / 30)
        self._energia = energia(esc.get_energia_vital() * self._parrilla_poderes[3])
        Superheroes.numero_superheroes += 1

        # la ultima linea nos dice donde se encuentra el heroe en la lista, cuando creamos la lista para el combate

    def get_identificador(self):
        return self._identificador

    def get_alias(self):
        return self._alias

    def get_movimientos(self):
        return self._movimientos

    def get_tipo(self):
        return self._tipo

    def get_parrillapoderes(self):
        return self._parrilla_poderes

    def get_coste(self):
        return self._coste

    def get_energia(self):
        return self._energia

    # creamos un metodo para que los movimientos adquieran ciertas estadisticas en funcion del tipo y comprobamos si es compatible con el superheroe
    def set_movimientos(self, x):
        for movimiento in x:
            if movimiento.get_tipo().value:
                movimiento.set_daño((movimiento.get_daño() / 10) * (
                            0.8 * self._parrilla_poderes[1] + 0.25 * self._parrilla_poderes[2] + 0.75 *
                            self._parrilla_poderes[5] + self._parrilla_poderes[4]))
            else:
                movimiento.set_daño((movimiento.get_daño() / 10) * (
                            self._parrilla_poderes[0] + 0.75 * self._parrilla_poderes[2] + 0.25 *
                            self._parrilla_poderes[5] + 0.2 * self._parrilla_poderes[1]))
            self._movimientos.append(movimiento)

    # establecemos la energia.
    def set_energia(self, x):
        try:
            if energia < 5 or energia >= 20:
                raise Exception("error en la energia., debe ser entre 0  y 20")

            self._energia = x
        except Exception as error:
            print(error)

    # creamos el metodo de defensa para que al atacar otro pokemon, este reciba daño
    def fight_defense(self, daño):
        self._energia -= daño
        if self._energia <= 0:
            self.die()

    # creamos el metodo ataque que obliga a un pokemon a usar el metodo de defensa creado antes para que este pierda vida
    # debido al ataque.
    def fight_attack(self, obj):
        obj.fight_defense(self._daño)




