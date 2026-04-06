
def factorial(n):
    if n >= 0:
        resultado = 1
        if n > 1:
            resultado = n * factorial(n - 1)
        return resultado
    else:
        raise ValueError("El factorial solo existe para numeros positivos.")

def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])
    

if __name__ == "__main__":
    # n = int(input())
    # m = int(input())
    lista = list(map(int, input().split()))

    # print(factorial(n))
    print(suma_lista(lista))
