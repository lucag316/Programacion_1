# Desafío #00:

# A. Analizar detenidamente el set de datos
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
# la altura del mismo
# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# F. Recorrer la lista y determinar la altura promedio de los superhéroes
# (PROMEDIO)
# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (MÁXIMO, MÍNIMO)
# H. Calcular e informar cual es el superhéroe más y menos pesado.
# I. Ordenar el código implementando una función para cada uno de los valores
# informados.
# J. Construir un menú que permita elegir qué dato obtener
from data_stark_00 import lista_personajes

def normalizar_datos(lista_personajes:list):

    for personaje in lista_personajes:

        personaje["altura"] = float(personaje["altura"])
        personaje["peso"] = float(personaje["peso"])
        personaje["fuerza"] = int(personaje["fuerza"])
normalizar_datos(lista_personajes)
#----------------------A-----------------------------------
# for personaje in lista_personajes:
#     print(personaje)
#----------------------A-----------------------------------


#----------------------B-----------------------------------
# for personaje in lista_personajes:
#     print(personaje["nombre"])
#----------------------B-----------------------------------


#----------------------C-----------------------------------
# for personaje in lista_personajes:
#     nombre = personaje["nombre"]
#     altura = personaje["altura"]
#     print(f"Nombre: {nombre}    |   Altura: {altura}")
#----------------------C-----------------------------------


#----------------------D-----------------------------------
mas_alto = lista_personajes[0]
for personaje in lista_personajes:
    if personaje["altura"] > mas_alto["altura"]:
        mas_alto = personaje
print(f"El personaje mas alto es: {mas_alto}")
#----------------------D-----------------------------------


#----------------------E-----------------------------------
mas_bajo = lista_personajes[0]
for personaje in lista_personajes:
    if personaje["altura"] < mas_bajo["altura"]:
        mas_bajo = personaje
print(f"El personaje mas bajo es: {mas_bajo}")
#----------------------E-----------------------------------

#----------------------F-----------------------------------
# acumulador_alturas = 0
# promedio_altura = 0
# for personaje in lista_personajes:
#     acumulador_alturas += personaje["altura"]
    
# promedio_altura = acumulador_alturas / len(lista_personajes)

# print(f"La altura promedio es: {promedio_altura}")
#----------------------F-----------------------------------


#----------------------G-----------------------------------
print("Mas alto: {} \nMas bajo: {}".format(mas_alto["nombre"], mas_bajo["nombre"]))
#----------------------G-----------------------------------


#----------------------H-----------------------------------
mas_pesado = lista_personajes[0]
menos_pesado = lista_personajes[0]

for personaje in lista_personajes:
    if personaje["peso"] > mas_pesado["peso"]:
        mas_pesado = personaje
    
    if personaje["peso"] < menos_pesado["peso"]:
        menos_pesado = personaje

print(f"El personaje mas pesado es: {mas_pesado}")
print(f"El personaje menos pesado es: {menos_pesado}")

#----------------------H-----------------------------------

# while True:
#     menu = print("")
#     opcion = input("Ingrese una opcion: ")
    
#     match():
#         case "1":
#             pass
#         case "2":
#             pass
#         case "3":
#             break