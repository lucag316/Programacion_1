# 3) Copa pistón!!!
# Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
# Se pedirá el ingreso de:
# nombre
#  edad (mayor a 18)
# nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
#  cantidad de carreras ganadas (no pueden ser números negativos)
#  número del vehículo (no puede ser un número negativo)
# se necesita saber:
# *Nacionalidad del piloto más joven.
# *Cantidad de vehículos con número par.
# *Nombre del piloto con menos victorias y el número de auto impar.       (NO ENTENDI BIEN SI ES EL DE MENOS VICTORIAS Y A SU VEZ QUE SEA IMPAR)
# *Cantidad de pilotos mayores de 25 años con número de vehículo impar.
# *Nombre del piloto más joven con más victorias.
# *Nacionalidad del piloto más veterano con menos victorias.           (NO SE COMO HACER SIN REPETIR CODIGO)
# *Promedio de edad de los pilotos que tiene un vehículo con número par.

bandera_mas_veterano = False
bandera_mas_joven = False
bandera_menos_victorias = False
bandera_mas_victorias = False

contador_pares = 0
# contador_impares = 0

pilotos_mayores_impares = 0

edades_pares = 0
promedio_edad_pares = 0

for integrante in range(3): # si quiero que vaya del  1 al 10 (1, 11), el tercer parametro ej (1, 11, 2), va del 1 al 10 de 2 en 2
    nombre = input("\nIngrese el nombre del piloto: ")
    while nombre == "":
        nombre = input("ERROR, reingrese el nombre del piloto: ")

    edad = int(input("Ingrese la edad del piloto [+18]: "))
    while edad < 18:
        edad = int(input("ERROR, reingrese la edad del piloto [+18]: "))
    
    nacionalidad = input("Ingrese la nacionalidad del piloto [argentino], [ingles], [frances], [brasilero], [estadounidense]: ")
    while nacionalidad != "argentino" and nacionalidad != "ingles" and nacionalidad != "frances" and nacionalidad != "brasilero" and nacionalidad != "estadounidense":
        nacionalidad = input("ERROR, reingrese la nacionalidad del piloto [argentino], [ingles], [frances], [brasilero], [estadounidense]: ")

    carreras_ganadas = int(input("Ingrese la cantidad de carreras ganadas: "))
    while carreras_ganadas < 0:
        carreras_ganadas = int(input("ERROR, reingrese la cantidad de carreras ganadas [0 o mas]: "))

    numero_vehiculo = int(input("Ingrese el numero del vehiculo [0 o mas]: "))
    while numero_vehiculo < 0:
        numero_vehiculo = int(input("ERROR, reingrese el numero del vehiculo [0 o mas]: "))


    if bandera_mas_joven == False or edad < mas_joven:
        mas_joven = edad
        nacionalidad_mas_joven = nacionalidad
        bandera_mas_joven = True

        if bandera_mas_victorias == False or carreras_ganadas > mas_victorias:
            mas_victorias = carreras_ganadas
            piloto_joven_mas_victorias = nombre
            bandera_mas_victorias = True

    elif bandera_mas_veterano == False or edad > mas_veterano:
        mas_veterano = edad
        bandera_mas_veterano = True

        #if  NOSE COMO HACER SIN REPETIR (bandera_menos_victorias)

    if numero_vehiculo % 2 == 0:
        contador_pares += 1
        edades_pares += edad

    else:
        # contador_impares += 1
        if edad >= 25:
            pilotos_mayores_impares += 1
    
        if bandera_menos_victorias == False or carreras_ganadas < menos_victorias:
            menos_victorias = carreras_ganadas
            piloto_menos_victorias = nombre
            bandera_menos_victorias = True

promedio_edad_pares = edades_pares / contador_pares

print("\n-------------------------------------------------------------------------------------")
print("La nacionalidad del piloto mas joven es: {0}".format(nacionalidad_mas_joven))
print("La cantidad de vehiculos con numero par es: {0}".format(contador_pares))
print("Piloto con menos victorias: {0}".format(piloto_menos_victorias))
print("Cantidad de pilotos mayores de 25 años con número de vehículo impar: {0}".format(pilotos_mayores_impares))
print("Nombre del piloto más joven con más victorias: {0}".format(piloto_joven_mas_victorias))
#print("Nacionalidad del piloto más veterano con menos victorias: {0}".format())
print("Promedio de edad de los pilotos que tiene un vehículo con número par: {0}".format(promedio_edad_pares))
print("-------------------------------------------------------------------------------------\n")
