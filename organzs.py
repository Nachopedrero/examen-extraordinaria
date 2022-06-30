from enum import Enum
from re import S
import string

class Organizacion:
    def __init__(self, x, y):
        if type(x) != str:
            raise TypeError("Invalid type for attribute nombre")
        if type(y) != list:
            raise TypeError("Invalid type for attribute superheroes")
        if not y:
             raise ValueError("Invalid value for attribute superheroes")
        self._nombre = x
        self._superheroes= y

    def get_nombre(self):
        return self._nombre

    def get_superheroes(self):
        return self._superheroes

    def set_superheroes(self,x):
        self._superheroes = x

    #Los nombres no se pueden cambiar, pero los superheroes pueden cambiar de organizacion.
#comprobamos que los superheroes esten vivos
    def is_undefeated(self):
        x = False
        for i in range(len(self._superheroes)):
            if self._superheroes[i].is_alive():
                x = True
                break
        return x
#creamos el metodo rendirnos donde nos establecemos la energia en  0 .
    def surrender(self):
        for superheroe in self._superheroes:
            superheroe.set_energia(0)
#como los superheroes ya existen, para crearlos solo tenemos que buscarlos y sacarlos.
    def __str__(self):
        tp = ""
        for superheroe in self._superheroes:
            tp += str(superheroe.get_identificador()) + ". Alias: " + superheroe.get_alias() + ", Tipo:" +  superheroe.get_tipo().name + ", Coste:" + str(superheroe.get_coste()) + ", Energia:" + str(superheroe.get_energia()) + "\n"

        return tp
# establece los atributos del superheroe
    def __repr__(self):
        tr = ""
        for superheroe in self._superheroes:
            tr += superheroe.get_identificador() + "\t" + superheroe.get_tipo() + "\t" + superheroe.get_movimientos() + "\n"