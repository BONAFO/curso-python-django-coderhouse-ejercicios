def leer_numeros():
    """Lee la cantidad de números y la lista desde la entrada estándar."""
    n = int(input())
    numeros = list(map(float, input().split()))
    return numeros, n


def calcular_media(numeros):
    n= numeros[1]
    numeros = numeros[0]
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado / n

import math
def calcular_mediana(numeros):
    n= numeros[1]
    numeros = sorted(numeros[0])
    mitad = math.floor(n / 2)
    if len(numeros) % 2 == 0:
        return (numeros[mitad-1] + numeros[mitad]) / 2
    else:
        return numeros[mitad]



def imprimir_reporte(media, mediana):
    """Imprime la media y mediana con formato."""
    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")


def main():
    numeros = leer_numeros()
    media = calcular_media(numeros)
    mediana = calcular_mediana(numeros)
    imprimir_reporte(media, mediana)


if __name__ == "__main__":
    main()


