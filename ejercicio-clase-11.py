"""
Implementar with en el siguiente código:
def guardar(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "w")
        archivo.write("Python\n")
        archivo.write("Django\n")
    except Exception as error:
        print("Error:", repr(error))
    finally:
        archivo.close()

def leer(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "r")
        contenido = archivo.read()
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as error:
        print("Error:", repr(error))
    else:
        print(contenido)
    finally:
        archivo.close()

def main():
    archivo = "5_test.txt"
    guardar(archivo)
    leer(archivo)

if __name__ == "__main__":
    main()
"""


def guardar(nombre_archivo):
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Python   \n")
            archivo.write("Django\n")
    except Exception as error:
        print("Error:", repr(error))


def leer(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as error:
        print("Error:", repr(error))
    else:
        print(contenido)


def main():
    archivo = "5_test.txt"
    guardar(archivo)
    leer(archivo)


if __name__ == "__main__":
    main()
