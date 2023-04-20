from data_stark_00 import lista_personajes
import os

def normalizar_datos(lista_personajes:list):
    """
    Recibe una lista
    
    Pasa cada valor a su tipo verdadero
    """
    for personaje in lista_personajes:

        personaje["altura"] = float(personaje["altura"])
        personaje["peso"] = float(personaje["peso"])
        personaje["fuerza"] = int(personaje["fuerza"])
normalizar_datos(lista_personajes)
#----------------------A-----------------------------------
def analizar_datos(lista_personajes: list):
    """
    Recibe una lista
    
    La recorre e imprime todos los elementos
    """
    for personaje in lista_personajes:
        print(personaje)
#----------------------A-----------------------------------

#----------------------B-----------------------------------
def imprimir_nombres(lista_personajes:list):
    """
    Recibe una lista
    
    La recorre e imprime el nombre de todos los elementos
    """
    for personaje in lista_personajes:
        print(personaje["nombre"])
#----------------------B-----------------------------------

#----------------------C-----------------------------------
def imprimir_nombres_alturas(lista_personajes:list):
    """
    Recibe una lista
    
    La recorre e imprime el nombre y la altura de todos los elementos
    """
    for personaje in lista_personajes:
        nombre = personaje["nombre"]
        altura = personaje["altura"]
        print(f"Nombre: {nombre}    |   Altura: {altura}")
#----------------------C-----------------------------------

#----------------------D-----------------------------------
def calcular_max(lista_personajes:list):
    """
    Recibe una lista
    
    La recorre y calcula cuales o cual es mas  alto
    """
    mas_alto = lista_personajes[0]
    for personaje in lista_personajes:
        if personaje["altura"] > mas_alto["altura"]:
            mas_alto = personaje
    for personaje in lista_personajes:
        if personaje["altura"] == mas_alto["altura"]:
            print(f"El personaje mas alto es: {mas_alto}")
#----------------------D-----------------------------------

#----------------------E-----------------------------------
def calcular_min(lista_personajes:list):
    """
    Recibe una lista
    
    La recorre y calcula cuales o cual es mas  bajo
    """
    mas_bajo = lista_personajes[0]
    for personaje in lista_personajes:
        if personaje["altura"] < mas_bajo["altura"]:
            mas_bajo = personaje
    for personaje in lista_personajes:
        if personaje["altura"] == mas_bajo["altura"]:
            print(f"El personaje mas bajo es: {mas_bajo}")
#----------------------E-----------------------------------

#----------------------F-----------------------------------
def calcular_promedio(lista_personajes:list) -> float:
    """
    Recine una lista
    
    Calcula el promedio de altura de los personajes
    
    Devuelve el promedio(float)
    """
    acumulador_alturas = 0
    promedio_altura = 0
    for personaje in lista_personajes:
        acumulador_alturas += personaje["altura"]
        
    promedio_altura = acumulador_alturas / len(lista_personajes)
    return promedio_altura
#----------------------F-----------------------------------

#----------------------G-----------------------------------
def calcular_nombre_anteriores():
    #print("Mas alto: {} \nMas bajo: {}".format(mas_alto["nombre"], mas_bajo["nombre"]))
    pass
#----------------------G-----------------------------------

#----------------------H-----------------------------------
def calcular_mas_y_menos_pesado(lista_personajes:list):
    """
    Recibe una lista
    
    La recorre y calcula cuales o cual es mas o menos pesado
    """
    mas_pesado = lista_personajes[0]
    menos_pesado = lista_personajes[0]

    for personaje in lista_personajes:
        if personaje["peso"] > mas_pesado["peso"]:
            mas_pesado = personaje
        if personaje["peso"] < menos_pesado["peso"]:
            menos_pesado = personaje
            
    for personaje in lista_personajes:
        if personaje["peso"] == mas_pesado["peso"]:
            print(f"El personaje mas pesado es: {mas_pesado}")
        if personaje["peso"] == menos_pesado["peso"]:
            print(f"El personaje menos pesado es: {menos_pesado}")
#----------------------H-----------------------------------

while True:
    os.system("cls")
    menu = print("""
        =========================================
            ***** MENU DE OPCIONES *****
        =========================================
        1- Analizar detenidamente el set de datos
        2- Nombre de cada personaje
        3- Nombre y altura de cada personaje
        4- Personaje mas alto
        5- Personaje mas bajo
        6- Altura promedio
        7- Solo nombre del mas alto y mas bajo
        8- personaje mas y menos pesado
        9- Salir
        =========================================
            """)
    opcion = input("Ingrese una opcion: ")
    
    match(opcion):
        case "1":
            analizar_datos(lista_personajes)
        case "2":
            imprimir_nombres(lista_personajes)
        case "3":
            imprimir_nombres_alturas(lista_personajes)
        case "4":
            calcular_max(lista_personajes)
        case "5":
            calcular_min(lista_personajes)
        case "6":
            promedio = calcular_promedio(lista_personajes)
            print(f"El promedio de altura es: {promedio}")
        case "7":
            calcular_nombre_anteriores()
        case "8":
            calcular_mas_y_menos_pesado(lista_personajes)
        case "9":
            confirmacion = input("Esta seguro? s/n: ")
            if confirmacion == "s":
                break
            else: 
                pass
    os.system("pause")
    
# EL PUNTO G FALTA