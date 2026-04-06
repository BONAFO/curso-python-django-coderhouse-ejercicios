"""
Crear una función que reciba un nombre y apellido.
Otra función que muestre este nombre y apellido de la siguiente forma:
    APELLIDO, nombre
"""

def get_user_data ():
    return input().split(" ")


def show_user_data (nombre:str, apellido:str):
    print(f"{apellido.upper()}, {nombre}")
    return

def main():
    nombre , apellido = get_user_data()
    show_user_data(nombre=nombre, apellido=apellido)

main()