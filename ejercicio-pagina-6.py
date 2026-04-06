class SumaExcesivaError(Exception):
    pass

def procesar_numeros():
    # Leer línea de entrada
    linea = input()
    numeros = linea.split()
    suma = 0
    try:
        for num_str in numeros:
            try:
                num = int(num_str)
            except ValueError:
                print(f"Error: '{num_str}' no es un entero válido.")
                continue
            suma += num
        if suma > 100:
            raise SumaExcesivaError
    except SumaExcesivaError:
        print("Error: Suma excesiva.")
    else:
        print(f"Suma total: {suma}")
    finally:
        print("Fin del procesamiento.")


if __name__ == "__main__":
    procesar_numeros()
