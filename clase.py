
class Usuario:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
    # def get_nombre(self):
    #     return self.__nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_valor: str): 
        if not nuevo_valor:
            raise ValueError("No puede estar vacío")
        self.__nombre = nuevo_valor
        
    # def set_nombre(self, nuevo_valor: str): 
    #     if not nuevo_valor:
    #         raise ValueError("No puede estar vacío")
    #     self.__nombre = nuevo_valor

usuario_1 = Usuario("admin")
print(usuario_1.__dict__)
usuario_1.nombre = "superadmin"
print(usuario_1.__dict__)
print(usuario_1.nombre)