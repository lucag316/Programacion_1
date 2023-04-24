# Desafío #01:
# Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
# utilizando un menú que permita acceder a cada uno de los puntos por separado.
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F
# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia

from data_stark import lista_personajes

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

def mostrar_personaje(personaje:dict):
    '''
    Muestra prolijamente el personaje que recibe
    '''
    print("\nNombre: {0} \nIdentidad: {1} \nEmpresa: {2} \nAltura: {3} \nPeso: {4} \nGenero: {5} \nColor de ojos: {6} \nColor de pelo: {7} \nFuerza: {8} \nInteligencia: {9}\n".format(personaje["nombre"], personaje["identidad"], personaje["empresa"], personaje["altura"], personaje["peso"], personaje["genero"], personaje["color_ojos"], personaje["color_pelo"], personaje["fuerza"], personaje["inteligencia"]))

#--------------------------------------------*** PUNTO A ***--------------------------------------------------------
def imprimir_masculinos(lista_heroes:list):
    for heroe in lista_heroes:
        if heroe["genero"] == "M":
            print("Nombre: {0}".format(heroe["nombre"]))
#--------------------------------------------*** PUNTO A ***--------------------------------------------------------

#--------------------------------------------*** PUNTO B ***--------------------------------------------------------
def imprimir_femeninos(lista_heroes:list):
    for heroe in lista_heroes:
        if heroe["genero"] == "F":
            print("Nombre: {0}".format(heroe["nombre"]))
#--------------------------------------------*** PUNTO B ***--------------------------------------------------------

#--------------------------------------------*** PUNTO C ***--------------------------------------------------------
def calcular_mayor_masculino(lista_heroes:list) -> dict:
    masculino_mayor_altura = lista_heroes[0]
    for heroe in lista_heroes:
        if heroe["genero"] == "M" and heroe["altura"] > masculino_mayor_altura["altura"]:
            masculino_mayor_altura = heroe
    return masculino_mayor_altura
#--------------------------------------------*** PUNTO C ***--------------------------------------------------------

#--------------------------------------------*** PUNTO D ***--------------------------------------------------------
def calcular_mayor_femenino(lista_heroes:list):
    femenino_mayor_altura = lista_heroes[0]
    for heroe in lista_heroes:
        if heroe["genero"] == "F" and heroe["altura"] > femenino_mayor_altura["altura"]:
            femenino_mayor_altura = heroe
    return femenino_mayor_altura
#--------------------------------------------*** PUNTO D ***--------------------------------------------------------

#--------------------------------------------*** PUNTO E ***--------------------------------------------------------
def calcular_menor_masculino(lista_heroes:list):
    masculino_menor_altura = lista_heroes[0]
    for heroe in lista_heroes:
        if heroe["genero"] == "M" and heroe["altura"] < masculino_menor_altura["altura"]:
            masculino_menor_altura = heroe
    return masculino_menor_altura
#--------------------------------------------*** PUNTO E ***--------------------------------------------------------

#--------------------------------------------*** PUNTO F ***--------------------------------------------------------
def calcular_menor_femenino(lista_heroes:list):
    #femenino_menor_altura = lista_heroes[0]      #NO FUNCIONA PORQUE EL PRIMERO DE LA LISTA ES MASCULINO
    bandera_femenino_menor = False
    for heroe in lista_heroes:
        if heroe["genero"] == "F" and heroe["altura"] < femenino_menor_altura["altura"]:
            femenino_menor_altura = heroe
    return femenino_menor_altura
#--------------------------------------------*** PUNTO F ***--------------------------------------------------------

#--------------------------------------------*** PUNTO G ***--------------------------------------------------------
def Calcular_promedio_altura_masculino(lista_heroes:list) -> float:
    cantidad_masculinos = 0
    acumulador_alturas_m = 0
    promedio_altura_m = 0
    
    for heroe in lista_heroes:
        if heroe["genero"] == "M":
            acumulador_alturas_m += heroe["altura"]
            cantidad_masculinos += 1
    promedio_altura_m = acumulador_alturas_m / cantidad_masculinos
    return promedio_altura_m
#--------------------------------------------*** PUNTO G ***--------------------------------------------------------

#--------------------------------------------*** PUNTO H ***--------------------------------------------------------
def Calcular_promedio_altura_femenino(lista_heroes:list) -> float:
    cantidad_femeninos = 0
    acumulador_alturas_f = 0
    promedio_altura_f = 0
    
    for heroe in lista_heroes:
        if heroe["genero"] == "F":
            acumulador_alturas_f += heroe["altura"]
            cantidad_femeninos += 1
    promedio_altura_f = acumulador_alturas_f / cantidad_femeninos
    return promedio_altura_f
#--------------------------------------------*** PUNTO H ***--------------------------------------------------------

#--------------------------------------------*** PUNTO I ***--------------------------------------------------------
#--------------------------------------------*** PUNTO I ***--------------------------------------------------------

#--------------------------------------------*** PUNTO J ***--------------------------------------------------------
def mostrar_tipo(lista_heroes:list, atributo:str) -> list:
    """
    Brief: Crea una lista con los distintos tipos de atributos
    
    Parameters: 
        lista_heroes: list -> lista sobre la que voy a hacer la  busqueda de los atributos
        atributo: str -> la clave del diccionario de donde voy a sacar los datos
        
    Return: Una list nueva con los distintos tipos de la variable ingresada
    """
    
    if type(lista_heroes) == list and len(lista_heroes) > 0 and type(atributo) == str and len(atributo) > 0:
        lista_tipo = []
        for heroe in lista_heroes:
            lista_tipo.append(heroe[atributo])
        return lista_tipo


def Calcular_cantidad_tipo(lista_heroes:list, atributo: str):
    """
    
    """
    if type(lista_heroes) == list and len(lista_heroes) > 0 and type(atributo) == str and len(atributo) > 0:
        diccionario = {}
        tipos = mostrar_tipo(lista_heroes, atributo)
        
        for tipo in set(tipos):
            contador = 0
            for heroe in lista_heroes:
                if tipo == heroe[atributo]:
                    if tipo == "" and atributo == "inteligencia":
                        tipo = "No tiene"
                    contador += 1
            diccionario[tipo] = contador
        return diccionario
        
def mostrar_lista(diccionario: dict):
    for clave in diccionario:
        print(f"{clave}: {diccionario[clave]}")

mostrar_lista(Calcular_cantidad_tipo(lista_personajes, "color_ojos"))
#--------------------------------------------*** PUNTO J ***--------------------------------------------------------
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.

def mostrar_heroes_por_tipo():
    pass
#--------------------------------------------*** PUNTO M ***--------------------------------------------------------
# M. Listar todos los superhéroes agrupados por color de ojos.


# while True:
#     os.system("cls")
#     menu = print("""
#         =========================================
#             ***** MENU DE OPCIONES *****
#         =========================================
#         1- Analizar detenidamente el set de datos
#         2- Nombre de cada personaje
#         3- Nombre y altura de cada personaje
#         4- Personaje mas alto
#         5- Personaje mas bajo
#         6- Altura promedio
#         7- Solo nombre del mas alto y mas bajo
#         8- personaje mas y menos pesado
#         9- Salir
#         =========================================
#             """)
#     opcion = input("Ingrese una opcion: ")
    
#     match(opcion):
#         case "1":
#             analizar_datos(lista_personajes)
#         case "2":
#             imprimir_nombres(lista_personajes)
#         case "3":
#             imprimir_nombres_alturas(lista_personajes)
#         case "4":
#             calcular_max(lista_personajes)
#         case "5":
#             calcular_min(lista_personajes)
#         case "6":
#             promedio = calcular_promedio(lista_personajes)
#             print(f"El promedio de altura es: {mostrar_personaje(promedio)}")
#         case "7":
#             calcular_nombre_anteriores()
#         case "8":
#             calcular_mas_y_menos_pesado(lista_personajes)
#         case "9":
#             confirmacion = input("Esta seguro? s/n: ")
#             if confirmacion == "s":
#                 break
#             else: 
#                 pass
#     os.system("pause")

# ARREGLAR EL PUNTO F
