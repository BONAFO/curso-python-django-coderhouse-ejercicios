"""


Crear una clase llamada Persona que tenga dos variables de instancia: nombre y apellido
Crear 2 instancias de Persona y mostrar sus variables con print()
- Crear un método de instancia "caminar" que reciba la cantidad de pasos
- El método puede ser llamado por cualquier instancia y puedo pasarle un número (cantidad de pasos)
- El método imprime el nombre de la persona y la cantidad de pasos que da
"""


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def print(self):
        msj = f"Datos Persona"
        for dato in self.__dict__:
            msj += f" {dato.capitalize()}: {self.__getattribute__(dato)}"
        print(msj)

    def caminar(self, pasos=0):
        try:
            match pasos:
                case 0:
                    print(f"{self.nombre} no esta caminando.")
                case 1:
                    print(f"{self.nombre} ha caminado {pasos} paso.")
                case pasos if pasos > 0:
                    print(f"{self.nombre} ha caminado {pasos} pasos.")
                case _:
                    raise ValueError("Solo puedes caminar valores positivos!")
        except TypeError:
            raise ValueError("Solo puedes caminar valores positivos... Y NUMERICOS!!")

    def keys():
        return ["Nombre", "Apellido"]


def listar_personas(personas=[Persona]):
    for k, p in enumerate(personas):
        p.print()


def main():
    p1 = Persona("Tina", "Perez")
    p2 = Persona("Naomi", "Martinez")
    listar_personas([p1, p2])
    p1.caminar(0)


main()
