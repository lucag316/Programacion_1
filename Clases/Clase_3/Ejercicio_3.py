# EJERCICIO 3 CLASE 3
# Es la gala final de Gran Hermano y la producción nos pide un programa para contar
# los votos de los televidentes y saber cuál será el participante que ganará el juego.
# Los participantes finalistas son: Nacho, Julieta y Marcos.
# El televidente debe ingresar:
# ● Nombre del votante
# ● Edad del votante (debe ser mayor a 13)
# ● Género del votante (masculino, femenino, otro)
# ● El nombre del participante a quien le dará el voto positivo.
# No se sabe cuántos votos entrarán durante la gala.
# Se debe informar al usuario:
# A. El promedio de edad de las votantes de género femenino
# B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
# Nacho o Julieta.
# C. Nombre del votante más joven que votó a Nacho.
# D. Nombre de cada participante y porcentaje de los votos qué recibió.
# E. El nombre del participante que ganó el reality (El que tiene más votos)

respuesta = "si"

cantidad_femeninos = 0
masculinos_especiales = 0

contador_nacho = 0
contador_julieta = 0
contador_marcos = 0

edades_femenino = 0

promedio_edad_femenino = 0

bandera_mas_joven_nacho = False

while respuesta == "si":
    nombre = input("\nIngrese el nombre del votante: ")
    while nombre == "":
        nombre = input("ERROR, reingrese el nombre del votante: ")

    edad = int(input("Ingrese la edad del votante [+13]: "))
    while edad < 13:
        edad = int(input("ERROR, reingrese la edad del votante [+13]: "))
    
    genero = input("Ingrese el genero del votante [masculino], [femenino], [otro]: ")
    while genero != "masculino" and genero !="femenino" and genero != "otro":
        genero = input("ERROR, reingrese el genero del votante [masculino], [femenino], [otro]: ")
    
    participante_votado = input("Ingrese el nombre del participante [nacho], [julieta], [marcos]: ")
    while participante_votado != "nacho" and participante_votado != "julieta" and participante_votado != "marcos":
        participante_votado = input("ERROR, reingrese el nombre del participante [nacho], [julieta], [marcos]: ")


    if genero == "femenino":
        cantidad_femeninos += 1
        edades_femenino += edad

    elif genero == "masculino" and edad > 24 and edad < 41:
        if participante_votado == "nacho" or participante_votado == "julieta": # if participante_votado != "marcos" ES LO MISMO
            masculinos_especiales += 1



    match participante_votado:
        case "nacho":
            if bandera_mas_joven_nacho == False or edad < mas_joven:
                mas_joven = edad
                votante_mas_joven_nacho = nombre
                bandera_mas_joven_nacho = True
                contador_nacho += 1
        case "julieta":
            contador_julieta += 1
        case "marcos":
            contador_marcos += 1
            
    respuesta = input("[si] para continuar \n[otra tecla] para salir \n")

promedio_edad_femenino = edades_femenino / cantidad_femeninos

contador_total = contador_nacho + contador_julieta + contador_marcos
porcentaje_nacho = (contador_nacho * 100) / contador_total
porcentaje_julieta = (contador_julieta * 100) / contador_total
porcentaje_marcos = (contador_marcos * 100) / contador_total

if contador_nacho > contador_julieta and contador_nacho > contador_marcos:
    print("El gandor es nacho")
elif contador_julieta > contador_nacho and contador_julieta > contador_marcos:
    print("La  ganadora es julieta")
else:
    print("El gandor es marcos")
    
    
print("El promedio de edad de las votantes de género femenino es: {0}".format(promedio_edad_femenino))
print("Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o : {0}".format(masculinos_especiales))
print("El nombre del votante más joven que votó a Nacho es: {0}".format(votante_mas_joven_nacho))
print("Nacho saco el {0}% ".format(porcentaje_nacho))
print("Julieta saco el {0}% ".format(porcentaje_julieta))
print("Marcos saco el {0}% \n".format(porcentaje_marcos))