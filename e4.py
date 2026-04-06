# Pedir al usuario su edad.
# Si es mayor o igual a 18, imprimir "eres mayor de edad"
# De lo contrario, imprimir "eres menor de edad"


def pedir_edad():
    try:
        edad= int(input("¿Que edad tenes?"))
        if(edad <= 120 and edad >= 0) :
            if(edad >= 18):
                print("eres mayor de edad")
            else:
                print("eres menor de edad")
        else:
            pedir_edad()
    except Exception as error:
        pedir_edad()


pedir_edad()