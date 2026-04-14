try:
    archivo = open("5_test.txt", "w")
    archivo.write("Python\n")
    archivo.write("Django\n")
    archivo.close()

    archivo = open("5_test.tx", "r")
    contenido = archivo.read()
    archivo.close()
    print(contenido)
except FileNotFoundError:
    raise FileNotFoundError("el archivo no existe")