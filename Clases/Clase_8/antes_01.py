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
import os

lista_copiada = []
for personaje in lista_personajes:
    lista_copiada.append(personaje.copy())

# def copiar_lista(lista: list):
#     lista_copiada = []
#     for elemento in lista:
#         lista_copiada.append(elemento.copy())
        
#     return lista_copiada

# lista_copiada = copiar_lista(lista_personajes)

def normalizar_datos(lista_heroes: list):
    """
    Recibe una lista
    
    Pasa cada valor a su tipo verdadero
    """
    for personaje in lista_heroes:

        personaje["altura"] = float(personaje["altura"])
        personaje["peso"] = float(personaje["peso"])
        personaje["fuerza"] = int(personaje["fuerza"])
normalizar_datos(lista_copiada)

def crear_lista_femeninos(lista_heroes: list) -> list:
    lista_femeninos = []
    for heroe in lista_heroes:
        if heroe["genero"] == "F":
            lista_femeninos.append(heroe)
    return lista_femeninos
def crear_lista_masculinos(lista_heroes: list) -> list:
    lista_masculinos = []
    for heroe in lista_heroes:
        if heroe["genero"] == "M":
            lista_masculinos.append(heroe)
    return lista_masculinos

lista_femeninos = crear_lista_femeninos(lista_copiada)
lista_masculinos = crear_lista_masculinos(lista_copiada)


def mostrar_personaje(personaje:dict):
    '''
    Brief: Muestra prolijamente el diccionario del personaje que recibe
    
    Parameters:
        personaje: dict -> el diccionario del personaje que se quiere mostrar
    
    Return: No retorna nada, imprime
    '''
    print("""
    Nombre: {0} 
    Identidad: {1} 
    Empresa: {2} 
    Altura: {3} 
    Peso: {4} 
    Genero: {5} 
    Color de ojos: {6} 
    Color de pelo: {7} 
    Fuerza: {8} 
    Inteligencia: {9}
    """.format(personaje["nombre"], 
            personaje["identidad"],
            personaje["empresa"], 
            personaje["altura"], 
            personaje["peso"], 
            personaje["genero"], 
            personaje["color_ojos"], 
            personaje["color_pelo"], 
            personaje["fuerza"], 
            personaje["inteligencia"]))
    return ("------------------------------------")

def mostrar_lista(lista: list, titulo: str) -> None:
    """
    Brief: Muestra la lista mas prolija con su item y con un titulo (como un print pero mas prolijo)
    
    Parameters:
        lista: list -> lista que quiero mostrar
        titulo: str -> Titulo que le quiero poner a la lista
        
    Return: No retorna nada, imprime
    """
    if type(lista) == type([]) and type(titulo) == type("") and len(lista) > 0:
        print("--------------------------------------")
        print(f"   ****** {titulo} *****")
        print("--------------------------------------")
        for item in lista:
            print(item)
        print("--------------------------------------")






def filtrar_heroe(lista_heroes:list, clave: str, valor: str) -> list:
    """
    Brief: Filtra la lista que le pasas segun los parametros que le pases, creando una lista nueva y va agregando el diccionario del personaje si cumple con los parametros
    
    Parameters:
        lista_heroes: list -> La lista de diccionarios que quiero filtrar
        clave: str -> La clave/key que quiero filtrar
        valor: str -> El  valor que quiero que este en la nueva lista
        
    Return: Retorna la lista de diccionarios filtrada
    """
    if(type(lista_heroes) == type([]) and type(clave) == type("") and type(valor) == type("") and len(lista_heroes) > 0):
        lista_filtrada = []
        for heroe in lista_heroes:
            if heroe[clave] == valor:
                lista_filtrada.append(heroe)
        return lista_filtrada

def proyectar_heroes(lista_heroes: list, clave: str) -> list:
    """
    Brief:
    
    Parameters:
        lista_heroes: list -> La lista de diccionarios que quiero filtrar
        clave: str -> La clave que quiero filtrar
        
    Return: Retorna la lista filtrada
    """
    lista_filtrada = []
    for heroe in lista_heroes:
        lista_filtrada.append(heroe[clave])
    
    return lista_filtrada



def esta_en_la_lista(lista: list, item: str) -> bool:
    """
    Brief: Te devuelve si el item esta o no esta en a lista
    
    Parameters:
        lista: list -> la lista en la que se va a buscar
        item: str -> el item que se va a buscar en la lista
    
    Return: Si esta en la lista te retorna "True", si no esta "False"
    """
    esta = False
    
    for elemento in lista:
        if elemento == item:
            esta = True
            break
        
    return esta



def imprimir_nombres_segun_genero(lista_heroes: list, genero: str):
    """
    brief: Imprime solo los nombres de una lista segun los parametros que ingreses
    
    Parameters:
        lista-heroes: list -> la lista sobre la cual se imprimiran los nombres
        genero: str -> depende que genero ingresemos seran los nombres que se van a imprimir
        
    Return: No retorna nada, imprime

    """
    if(type(lista_heroes) == type([]) and type(genero) == type("") and len(lista_heroes) > 0):
        for heroe in lista_heroes:
            if heroe["genero"] == genero:
                print("Nombre: {0}".format(heroe["nombre"]))

def calcular_max_min(lista_heroes: list, condicion: str, clave: str) -> dict:
    """
    brief: Calcula cual es el maximo o el minimo de una lista de diccionarios(depende de los parametros que ingreses).
    Tambien llama a la funcion "mostra_personaje" para que lo que retorne se vea prolijo
    
    Parameters: 
        lista_heroes: list -> sobre la lista que voy a calcular
        condicion: str -> ingresar ("max" o "min ") para buscar el mayor o menor de la lista
        clave: str -> sobre lo que quiero calcular("altura", "peso", etc)
    
    Return: Retorna el diccionario del heroe segun el calculo que se hizo
    """
    if(type(lista_heroes) == type([]) and type(condicion) == type("") and type(clave) == type("") and len(lista_heroes) > 0):
        
        max_min = lista_heroes[0]
        
        for heroe in lista_heroes:
            if condicion == "max" and heroe[clave] > max_min[clave]:
                max_min = heroe
            if condicion == "min" and heroe[clave] < max_min[clave]:
                max_min = heroe
                
        max_min = mostrar_personaje(max_min)
        return max_min

def calcular_promedio(lista_heroes:list, genero:str, clave: str) -> float:
    """ 
    Brief: calcula el promedio de algo segun los parametros que se pasen
    
    Parameters:
        lista_heroes: list -> lista en la cual se va a realizar el promedio
        genero: str -> se puede separar segun el genero "F", "M", etc
        clave: str -> La clave segun se va a realizar el promedio "altura", "peso", etc
    
    Return: Retorna el promedio (float)
    """
    if(type(lista_heroes) == type([]) and type(genero) == type("") and type(clave) == type("") and len(lista_heroes) > 0):
        cantidad= 0
        acumulador = 0
        promedio = 0
        
        for heroe in lista_heroes:
            if heroe["genero"] == genero:
                acumulador += heroe[clave]
                cantidad += 1
        promedio = acumulador / cantidad
        
        return promedio

def listar_agrupados_tipo(lista_heroes: list, clave: str):
    """
    Brief:
    
    Parameters:
        lista_heroes: list -> 
    
    Return: No retorna nada, imprime
    """
    if(type(lista_heroes) == type([]) and type(clave) == type("") and len(lista_heroes) > 0):
        
        tipos = []
        for heroe in lista_copiada:
            heroe[clave] = heroe[clave].upper()  # NO SE SI HICE BIEN ESTE RENGLON, CREO QUE SI, PERO NO SE PORQUE ME APARECE EN BLANCO EL upper
            if heroe[clave] not in tipos:
                tipo = tipos.append(heroe[clave]) 
        
        for tipo in tipos:
            print(tipo)
            for heroe in lista_heroes:
                if heroe[clave] == tipo:
                    print(heroe["nombre"])
            print("------------------------------")


# M. Listar todos los superhéroes agrupados por color de ojos.    


# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia
# FALTA EL PUNTO I

while True:
    os.system("cls")
    menu = print("""
        =========================================
            ***** MENU DE OPCIONES *****
        =========================================
        1- Imprimir nombres masculinos
        2- Imprimir nombres femeninos
        3- Masculino mas alto
        4- Femenino mas alto
        5- Masculino mas bajo
        6- Femenino mas bajo
        7- Promedio de altura de los masculinos
        8- Promedio de altura de los femeninos
        9- Solo los nombres de los puntos 3, 4, 5, 6
        10- Cantidad de cada tipo de color de ojos
        11- Cantidad de cada tipo de color de pelo
        12- Cantidad de cada tipo de inteligencia
        13- Listar agrupados por color de ojos.
        14- Listar agrupados por color de pelo.
        15- Listar agrupados por tipo de inteligencia
        16- Salir
        
        EXTRAS:
        20-
        =========================================
            """)
    opcion = input("Ingrese una opcion: ")
    
    match(opcion):
        case "1":
            imprimir_nombres_segun_genero(lista_copiada, "M")
        case "2":
            imprimir_nombres_segun_genero(lista_copiada, "F")
        case "3":
            print(calcular_max_min(lista_masculinos, "max", "altura"))
        case "4":
            print(calcular_max_min(lista_femeninos, "max", "altura"))
        case "5":
            print(calcular_max_min(lista_masculinos, "min", "altura"))
        case "6":
            print(calcular_max_min(lista_femeninos, "min", "altura"))
        case "7":
            print(calcular_promedio(lista_copiada, "M", "altura"))
        case "8":
            print(calcular_promedio(lista_copiada, "F", "altura"))
        case "9":
            pass
        case "10":
            pass
        case "11":
            pass
        case "12":
            pass
        case "13":
            listar_agrupados_tipo(lista_copiada, "color_ojos")
        case "14":
            listar_agrupados_tipo(lista_copiada, "color_pelo")
        case "15":
            listar_agrupados_tipo(lista_copiada, "inteligencia")
        case "16":
            confirmacion = input("Esta seguro? s/otra tecla: ")
            if confirmacion == "s":
                break
            else: 
                pass
        case "20":
            print(filtrar_heroe(lista_copiada, "genero", "F"))
    os.system("pause")







#------------------------------------------------------------------------------------------------------------
    # if(type(lista_heroes) == type([]) and type(clave) == type("") and len(lista_heroes) > 0):
        
    #     tipos = []
    #     for heroe in lista_copiada:
    #         heroe[clave] = heroe[clave].upper()  # NO SE SI HICE BIEN ESTE RENGLON, CREO QUE SI, PERO NO SE PORQUE ME APARECE EN BLANCO EL upper
    #         if heroe[clave] not in tipos:
    #             tipo = tipos.append(heroe[clave]) 
        
    #     for tipo in tipos:
    #         print(tipo)
    #         for heroe in lista_heroes:
    #             if heroe[clave] == tipo:
    #                 print(heroe["nombre"])
    #         print("------------------------------")
#------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------
    # PROYECTAR CLAVE BIEN pero lo mejore
    # if type(lista_heroes) == type([]) and type(clave) == type("") and len(lista_heroes) > 0:
        
    #     lista_filtrada = []
        
    #     for heroe in lista_heroes:
    #         lista_filtrada.append(heroe[clave])
        
    #     if not con_repe:
    #         lista_aux = []
    #         for item in lista_filtrada:
    #             if not esta_en_la_lista(lista_aux, item):
    #                 lista_aux.append(item)
    #         lista_filtrada = lista_aux
        
    #     return lista_filtrada
#------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------
    # colores = []
    # for heroe in lista_copiada:
    #     heroe["color_ojos"] = heroe["color_ojos"].capitalize()  # NO SE SI HICE BIEN ESTE RENGLON, CREO QUE SI, PERO NO SE PORQUE ME APARECE EN BLANCO EL capitalize
    #     if heroe["color_ojos"] not in colores:
    #         color = colores.append(heroe["color_ojos"]) 
    
    # for color in colores:
    #     print(f"Color: {color} \n")
    #     for heroe in lista_heroes:
    #         if heroe["color_ojos"] == color:
    #             print(heroe["nombre"])
    #     print("------------------------------")
#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------
# def mostrar_tipo(lista_heroes:list, atributo:str) -> list:
#     """
#     Brief: Crea una lista con los distintos tipos de atributos
    
#     Parameters: 
#         lista_heroes: list -> lista sobre la que voy a hacer la  busqueda de los atributos
#         atributo: str -> la clave del diccionario de donde voy a sacar los datos
        
#     Return: Una list nueva con los distintos tipos de la variable ingresada
#     """
    
#     if type(lista_heroes) == list and len(lista_heroes) > 0 and type(atributo) == str and len(atributo) > 0:
#         lista_tipo = []
#         for heroe in lista_heroes:
#             lista_tipo.append(heroe[atributo])
#         return lista_tipo

# def Calcular_cantidad_tipo(lista_heroes:list, atributo: str):
#     """
    
#     """
#     if type(lista_heroes) == list and len(lista_heroes) > 0 and type(atributo) == str and len(atributo) > 0:
#         diccionario = {}
#         tipos = mostrar_tipo(lista_heroes, atributo)
        
#         for tipo in set(tipos):
#             contador = 0
#             for heroe in lista_heroes:
#                 if tipo == heroe[atributo]:
#                     if tipo == "" and atributo == "inteligencia":
#                         tipo = "No tiene"
#                     contador += 1
#             diccionario[tipo] = contador
#         return diccionario
        
# def mostrar_lista(diccionario: dict):
#     for clave in diccionario:
#         print(f"{clave}: {diccionario[clave]}")

# mostrar_lista(Calcular_cantidad_tipo(lista_personajes, "color_ojos"))

# def mostrar_heroes_por_tipo():
#     pass
    #-------------------------------------------------------------------------------------------------


    #-------------------------------------------------------------------------------------------------
# def Calcular_promedio_altura_femenino(lista_heroes:list) -> float:
#     cantidad_femeninos = 0
#     acumulador_alturas_f = 0
#     promedio_altura_f = 0
    
#     for heroe in lista_heroes:
#         if heroe["genero"] == "F":
#             acumulador_alturas_f += heroe["altura"]
#             cantidad_femeninos += 1
#     promedio_altura_f = acumulador_alturas_f / cantidad_femeninos
#     return promedio_altura_f
    #-------------------------------------------------------------------------------------------------

#--------------------------------------------*** PUNTO C ***--------------------------------------------------------
# def calcular_mayor_masculino(lista_heroes:list) -> dict:
#     masculino_mayor_altura = lista_heroes[0]
#     for heroe in lista_heroes:
#         if heroe["genero"] == "M" and heroe["altura"] > masculino_mayor_altura["altura"]:
#             masculino_mayor_altura = heroe
#     return masculino_mayor_altura
#--------------------------------------------*** PUNTO C ***--------------------------------------------------------