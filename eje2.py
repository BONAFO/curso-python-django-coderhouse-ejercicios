# Descripción de la actividad.
# En nuestro trabajo, nos solicitan desarrollar un programa
# que permita calcular el promedio final de los equipos de fútbol en un torneo.
# Para ello, debemos considerar tres aspectos:
# Jugaron 20 partidos durante el torneo.
# Los partidos poseen diferente puntaje según el resultado:
# los partidos ganados 3 puntos, partido empatado 1 punto, partido perdido 0 puntos.
# El promedio final resulta de la cantidad de puntos totales divididos
# la cantidad de partidos.

def calcular_equipo(equipo=[]):
    promedio = 0
    partidos = 20

    for e in equipo: 
        promedio += e

    return promedio / partidos


res = calcular_equipo([3,1,1,1,0, 3,1,3,0,1, 3,1,3,1,0 ,  3,1,1,1,1])

print(res)
