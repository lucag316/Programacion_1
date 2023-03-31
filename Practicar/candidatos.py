"""
EJERCICIO 1
Ingresar el nombre de los 5 candidatos a presidente de CusCús,  la edad de cada uno y la cantidad
de votos (no menor a cero)  que sacó en las elecciones.
Informar: 
el candidato con más votos
el candidato con menos votos
el promedio de edades de los candidatos
total de votos emitidos.
"""
bandera_mayor_votos = False
mayor_cantidad_votos = 0

bandera_menor_votos = False
menor_cantidad_votos = 10000000000000

acumulador_edad = 0
cantidad_candidatos = 0

acumulador_votos = 0

for candidato in range(5):
    nombre = input("Ingrese el nombre del candidato: ")
    
    edad = int(input("Ingrese la edad del candidato: "))
    while edad < 0:
        edad = int(input("ERROR, reingrese la edad"))
        
    votos = int(input("Ingrese la cantidad de votos"))
    while votos < 0:
        votos = int(input("ERROR, reingrese la cantidad de votos"))

    if votos > mayor_cantidad_votos or bandera_mayor_votos == False:

        mayor_cantidad_votos = votos
        nombre_mayor_cantidad_votos = nombre
        bandera_mayor_votos = True

    if votos < menor_cantidad_votos or bandera_menor_votos == False:

        menor_cantidad_votos = votos
        nombre_menor_cantidad_votos = nombre
        bandera_menor_votos = True

    cantidad_candidatos += 1
    acumulador_edad = acumulador_edad + edad 
    acumulador_votos += votos

promedio_edades = acumulador_edad / cantidad_candidatos

print("El candidato con mas votos es: {0}".format(nombre_mayor_cantidad_votos))
print("El candidato con menos votos es: {0}".format(nombre_menor_cantidad_votos))
print("El promedio de edad es: {0}".format(promedio_edades))
print("Total de votos emitidos: {0}".format(acumulador_votos))