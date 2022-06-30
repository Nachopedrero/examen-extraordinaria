from Superheroes import *
from organizaciones import Organizacion
#creamos la lista con personajes:
firstNames = {"A":"Captain", "B":"Turbo", "C":"Galactic", "D":"The", "E":"Aqua", "F":"Fire",
"G":"Iron", "H":"Super", "I":"Green", "J":"Phantom", "K":"Dark", "L":"Ghost", "M":"Professor",
"N":"Atomic", "O":"Rock", "P":"Omega", "Q":"Rocket", "R":"Shadow", "S":"Agent", "T":"Silver",
"U":"Wild", "V":"Wolf", "W":"Ultra", "X":"Wonder", "Y":"Doctor", "Z":"Star"}

lastNames = {"A":"X", "B":"Shield", "C":"Machine", "D":"Justice", "E":"Beast", "F":"Wing",
"G":"Arrow", "H":"Skull","I":"Blade", "J":"Bolt", "K":"Cobra", "L":"Blaze",
"M":"Soldier", "N":"Strike", "O":"Falcon", "P":"Fang", "Q":"King", "R":"Surfer",
"S":"Bot", "T":"Guard", "U":"Thing", "V":"Claw", "W":"Brain", "X":"Master", "Y":"Power", "Z":"Storm"}

def main():

    #elegir escenario
    escenario = input("Elija un escenario de entre los siguientes: sanctum_sanctorum/ stark_tower/ xavier_school: ")

    escenario = #creamos el escenario en funcion de la clase(de que escenario)

    #crear superheroes

    nombrelist = list(firstNames.values())
    apellidolist = list(lastNames.values())
    tipolist = ["HUMANO", "NOHUMANO"]
    superlist = []

    for i in range (0,80):
        x = random.randint(0, len(nombrelist)-1)
        y = random.randint(0, len(apellidolist)-1)
        a = tipolist[random.randint(0,1)]

        tipo = Superheroe_Type.from_str(a)
        nombre = nombrelist[x] + " " + apellidolist[y]

        superlist.append(Superheroes(nombre, nombre, tipo, escenario))

    # crear organizaciones
    nombreorg = ["A - Force", "Avengers", "Mercs for Money", "League of Realms", "Strange Academy", "X-Men"]
    organizaciones = []
    for i in range(0, len(nombreorg)):
        organizaciones.append(Organizacion(nombreorg[i], superlist[10*i:10*(i+1)]))
    organizaciones.append(Organizacion("Independientes", superlist[10*len(nombreorg):]))

    # mostrar superheroes

    print("Estos son los superheres a elegir y sus costes: ")
    for organizacion in organizaciones:
        print(organizacion.get_nombre() + ": ")
        print(organizacion.__str__())




    #elegir golpes

    # faltaria el metodo principal del combate que cogeria un escenario, el numero de heroes monedas y energia de ese escenario,
    # establecidas por nostros al crear el escenario, y los pondria a atacarse constantemente en un while que compruebe que ambos siguen vivos.
    # en  el ataque se emplearian los metodos de defender y atacar que implican que la vida de ambos bajen en funcion del
    # ataque y defensas del rival y propias respectivamente.






if __name__ == "__main__":
    main()

