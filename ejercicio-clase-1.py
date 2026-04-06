def eliminar_duplicados(lista):
    # Implementa la función para eliminar duplicados manteniendo el orden
    pass

def comparar_listas(lista1, lista2):
    # Implementa la función para encontrar elementos comunes y diferencias
    pass

if __name__ == '__main__':
    # Lectura y ejecución para ejercicio 1
    # n = int(input())
    # lista = list(map(int, input().split()))
    n = 5
    lista = [3, 5, 3, 2, 5, 1]
    resultado = eliminar_duplicados(lista)
    print(' '.join(map(str, resultado)))

    # Lectura y ejecución para ejercicio 2
    m = int(input())
    lista1 = list(map(int, input().split()))
    k = int(input())
    lista2 = list(map(int, input().split()))
    comunes, solo_en_1, solo_en_2 = comparar_listas(lista1, lista2)
    print(' '.join(map(str, sorted(comunes))))
    print(' '.join(map(str, sorted(solo_en_1))))
    print(' '.join(map(str, sorted(solo_en_2))) )
