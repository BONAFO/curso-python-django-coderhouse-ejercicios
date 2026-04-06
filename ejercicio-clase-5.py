# Para aprobar un crédito, el cliente debe ser mayor de edad.
# Además, debe tener una antigüedad en el sistema financiero mínima de 3 años,
# y un ingreso mensual mayor a 2500 dólares. En caso de que no tenga la antigüedad
# suficiente, su ingreso mensual debe ser como mínimo 4000 dólares.
# Si no cumple ninguna de las condiciones, no se aprueba el crédito.


edad = int(input("Edad:"))
antiguedad = int(input("Antiguedad:"))
ingreso_men = int(input("Ingrso Mensual:"))

cond_1= edad >= 18
cond_2= antiguedad >= 3

if cond_1 and cond_2 and ingreso_men > 2500:
    print("Credito Aprobado!")
elif (cond_1 and ingreso_men >= 4000) and not cond_2:
    print("Credito Aprobado! 2")
else :
    print("Credito Rechazado...")