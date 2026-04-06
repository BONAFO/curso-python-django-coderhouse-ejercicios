def factorial(n):
    if n >= 0:
        resultado = 1
        if n > 1:
            resultado = n * factorial(n - 1)
        return resultado
    else:
        raise ValueError("El factorial solo existe para numeros positivos.")

num = int(input())
fact = factorial(num)
print(fact)
