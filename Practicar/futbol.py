"""
Ejercicio 1
Se pide cargar la ficha médica para 11 jugadores de fútbol.
Se solicita Nombre, Edad, Peso(ej: 60.5kg) y Altura(ej: 1.65mt).
A) Nombre del jugador más joven.
B) El peso del jugador más alto.
C) Promedio de altura del equipo.
D) Promedio de peso del equipo.
E) Cantidad de jugadores que superen 1.7 mt y pesen mas de 85 kg.
"""

bandera_mas_joven = False
edad_mas_joven = 10000000

bandera_mas_alto = False
mas_alto = 0

acumulador_altura = 0
acumulador_peso = 0

jugadores_grandes = 0

for jugador in range(3):
    nombre = input("\nIngrese el nombre del jugador: ")
    
    edad = int(input("Ingrese la edad del jugador: "))
    while edad < 0:
        edad = int(input("ERROR, reingrese la edad: "))

    peso = float(input("Ingrese el peso del jugador: "))
    while peso < 0:
        peso = float(input("ERROR, reingrese el peso: "))
    
    altura = float(input("Ingrese la altura del jugador: "))
    while altura < 0:
        altura = float(input("ERROR, reingrese la altura: "))
        
    if edad < edad_mas_joven or bandera_mas_joven == False:
        edad_mas_joven = edad
        nombre_mas_joven = nombre
        bandera_mas_joven == True

    if altura > mas_alto or bandera_mas_alto == False:

        mas_alto = altura
        peso_mayor_altura = peso
        bandera_mas_alto = True

    if altura > 1.7 and peso > 85:
        jugadores_grandes += 1

    acumulador_altura += altura
    acumulador_peso += peso

promedio_altura = acumulador_altura / 13
promedio_peso = acumulador_peso / 3

print("\nEl nombre del jugador mas joven es: {0}".format(nombre_mas_joven))
print("El peso del jugador mas alto es: {0}".format(peso_mayor_altura))
print("Promedio de altura: {0}".format(promedio_altura))
print("Promedio de peso: {0}".format(promedio_peso))
print("Cantidad de jugadores que pesan mas de 85 kg y superen 1.7 mt: {0}\n".format(jugadores_grandes))

# NO SALEN BIEN LOS RESULTADOS (CREO QUE LOS PROMEDIOS)