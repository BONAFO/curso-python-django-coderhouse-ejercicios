# Problema 1

def calcular_area(base, altura):
    # TODO: Implementar función que calcule el área del rectángulo
    return base * altura

if __name__ == '__main__':
    base, altura = map(float, input().split())
    print(int(calcular_area(base, altura)))

# Problema 2

def saludo_personalizado(nombre, edad=0):
    # TODO: Implementar función que retorne saludo personalizado
    if edad != 0:
        return f"Hola, {nombre}! Tienes {edad} años."
    else:
        return f"Hola, {nombre}!"

if __name__ == '__main__':
    entrada = input().split()
    if len(entrada) == 2:
        nombre, edad = entrada[0], int(entrada[1])
        print(saludo_personalizado(nombre, edad))
    else:
        nombre = entrada[0]
        print(saludo_personalizado(nombre))

# Problema 3

import math

def calcular_area_circulo(radio):
    # TODO: Calcular área del círculo
    return math.pi * radio ** 2

def formatear_area(area):
    # TODO: Formatear área con 2 decimales
    return f"Área: {area:.2f}"

if __name__ == '__main__':
    r = float(input())
    area = calcular_area_circulo(r)
    print(formatear_area(area))

# Problema 4

def suma_natural(n):
    # TODO: Implementar suma recursiva
    if n == 1:
        return 1
    else:
        return n + suma_natural(n - 1)

if __name__ == '__main__':
    n = int(input())
    print(suma_natural(n))   