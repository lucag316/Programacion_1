# EJERCICIO 2
# Se nos pide armar una aplicación para las elecciones, para eso necesitamos ingresar el nombre de los 5 candidatos a presidente de la nación,  la edad de cada uno (mayor a 35 años de edad) y la cantidad de votos (número positivo 0 incluido)  que sacó en las elecciones.
# Informar: 
# •	el candidato con más votos
# •	el candidato con menos votos
# •	el promedio de edades de los candidatos
# •	total de votos emitidos.
# •	el porcentaje de los votos de los 5 candidatos

bandera_mas_votos = False
bandera_menos_votos = False

acumulador_edades = 0
acumulador_votos = 0

for candidato in range(5):
    nombre = input("\nIngrese el nombre del candidato: ")
    while nombre == "":
        nombre = input("ERROR, reingrese el nombre del candidato: ")
     
    edad = int(input("Ingrese la edad del candidato: "))
    while edad < 35:
        edad = int(input("ERROR, reingrese la edad del candidato [+35]: "))
    
    votos = int(input("Ingrese la cantidad de votos: "))
    while votos < 0 :
        votos = int(input("ERROR, reingrese la cantidad de votos: "))
    
    if bandera_mas_votos == False or votos > mas_votos:
        nombre_mas_votos = nombre
        mas_votos = votos
        bandera_mas_votos = True
    
    if bandera_menos_votos == False or votos < menos_votos:
        menos_votos = votos
        nombre_menos_votos = nombre
        bandera_menos_votos = True
        
    acumulador_edades += edad
    acumulador_votos += votos

promedio_edades = acumulador_edades / 5

print("\n=================================================================================================================")
print("El candidato con mas votos es: {0}".format(nombre_mas_votos))
print("El candidato con menos votos es: {0}".format(nombre_menos_votos))
print("EL promedio de edades es: {0}".format(promedio_edades))
print("Total de votos emitidos: {0}".format(acumulador_votos))
#print("El porcentaje de los candiatros: {0}".format())
print("=================================================================================================================\n")

# CREO QUE EL ULTIMO SE USAN LISTAS