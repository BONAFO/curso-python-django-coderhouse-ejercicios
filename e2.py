"""
Crear un método de instancia para establecer una contraseña
"""


class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.nombre = nombre
        self.__contraseña = contraseña

    def __str__(self) -> str:
        return self.nombre

    def set_nombre(self, nuevo_valor: str):  # método de instancia
        if nuevo_valor:
            self.nombre = nuevo_valor
        else:
            raise ValueError("No puede estar vacío")

    def set_contraseña(self, nuevo_valor: str):  # método de instancia
        if nuevo_valor:
            if len(nuevo_valor) < 8:
                raise ValueError("La contraseña debe tener al menos 8 caracteres")
            self.nombre = nuevo_valor
        else:
            raise ValueError("No puede estar vacío")


def main():
    usuario_1 = Usuario("admin", "123")
    usuario_2 = Usuario("juan", "789")
    usuario_3 = Usuario("pepe", "555")
    usuarios = (usuario_1, usuario_2, usuario_3)
    for usuario in usuarios:
        print(usuario, end=" ")
    
    usuario_1.set_nombre("superadmin")
    usuario_1.set_contraseña("123uisd9as")
    for usuario in usuarios:
        print(usuario.__contraseña, end=" ")


main()
