from enum import Enum


class Escenarios:

    def __init__(self, monedas, miembros, movs, energiavital):
        self._monedas = monedas
        self._miermbrosekip = miembros
        self._movimientos = movs
        self._energiavital = energiavital

    def get_monedas(self):
        return self._monedas

    def get_miembros_ekip(self):
        return self._miermbros_ekip

    def get_movimientos(self):
        return self._movimientos

    def get_energia_vital(self):
        return self._energia_vital

    def from_str(x):

        escenario = x.lower()
        e = None

        for tp in TipoEscenario:
            if escenario == tp.name:
                a = tp.value
                e = Escenarios(a[0], a[1], a[2], a[3])
                break

        if type(e) != Escenarios:
            raise TypeError("Invalid type for attribute nombre")

        return e


# creamos las variaciones de los escenarios, con herencia de escenario.
class Sanctum_sanctorum(Escenarios):
    def __init__(self, monedas, miembros, movs, energiavital):
        try:
            if monedas < 100 or monedas >= 1000:
                raise Exception("demasiadas monedas")
        except Exception as error:
            print(error)
            self.monedas = monedas
            super().__init__(miembros, movs, energiavital)

    def get_monedas(self):
        return self._monedas

    def get_miembros_ekip(self):
        return self._miermbros_ekip

    def get_movimientos(self):
        return self._movimientos

    def get_energia_vital(self):
        return self._energia_vital


class Stark_tower(Escenarios):
    def __init__(self, monedas, miembros, energiavital):
        try:
            if movs < 10 or movs >= 30:
                raise Exception("demasiados movimientos")
        except Exception as error:
            print(error)
            self.movs = movs
            super().__init__(miembros, movs, energiavital)

    def get_monedas(self):
        return self._monedas

    def get_miembros_ekip(self):
        return self._miermbros_ekip

    def get_movimientos(self):
        return self._movimientos

    def get_energia_vital(self):
        return self._energia_vital


class Xavier_school(Escenarios):
    def __init__(self, monedas, miembros, movs, energiavital):
        try:
            if energiavital < 10 or energiavital >= 40:
                raise Exception("demasiada energia")
        except Exception as error:
            print(error)
            self.energiavital = energiavital
            super().__init__(miembros, movs, energiavital)

    def get_monedas(self):
        return self._monedas

    def get_miembros_ekip(self):
        return self._miermbros_ekip

    def get_movimientos(self):
        return self._movimientos

    def get_energia_vital(self):
        return self._energia_vital