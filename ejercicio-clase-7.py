"""
A partir de las siguientes funciones, crear una nueva función
que tenga como única responsabilidad tomar la lista de nombres y
usar for para llamar a la función saludar()
"""

def saludar(nombre: str):
    print(nombre)
    print("=" * len(nombre))

def bienvenida_a_todos(lista_nombres:list):
    for nombre in lista_nombres:
        saludar(nombre)
    

def main():
    lista_nombres = ("Claudio", "Nahir", "Alberto", "Matías")
    bienvenida_a_todos(lista_nombres)

main()