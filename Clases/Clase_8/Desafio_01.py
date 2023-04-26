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

def mostrar_personaje(personaje:dict) -> None:
    '''
    Brief: Muestra prolijamente el diccionario del personaje que recibe
    
    Parameters:
        personaje: dict -> el diccionario del personaje que se quiere mostrar
    
    Return: No retorna nada, imprime
    '''
    if type(personaje) == type({}):
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
        print("======================================")
        print(f"   ****** {titulo} *****")
        print("======================================")
        for item in lista:
            print(item)
        print("======================================")

def esta_en_la_lista(lista: list, item: str) -> bool:
    """
    Brief: Te devuelve si el item esta o no esta en a lista
    
    Parameters:
        lista: list -> la lista en la que se va a buscar
        item: str -> el item que se va a buscar en la lista
    
    Return: Si esta en la lista te retorna "True", si no esta "False"
    """
    if type(lista) == type([]) and type(item) == type("") and len(lista) > 0:
        esta = False
        
        for elemento in lista:
            if elemento == item:
                esta = True
                break
            
        return esta

def sacar_repetidos(lista: list) -> list:
    """
    brief: Saca los repetidos de una lista de elementos basicos, NO de diccionarios
    
    Parameters:
        lista: list -> La lista que quiero sacarle los repetidos
    
    returns: Retorna una lista sin repetidos
    """
    if type(lista) == type([]) and len(lista) > 0:
        lista_sin_repetidos = []
        
        for elemento in lista:
            if not esta_en_la_lista(lista_sin_repetidos, elemento):
                lista_sin_repetidos.append(elemento)
            
        return lista_sin_repetidos

def filtrar_heroe(lista_heroes:list, clave: str, valor: str) -> list:
    """
    Brief: Filtra la lista que le pasas segun los parametros que le pases, creando una lista nueva y va agregando el diccionario del personaje si cumple con los parametros
    
    Parameters:
        lista_heroes: list -> La lista de diccionarios que quiero filtrar
        clave: str -> La clave/key que quiero filtrar
        valor: str -> El  valor que quiero que este en la nueva lista
        
    Return: Retorna la lista de diccionarios filtrada
    """
    if type(lista_heroes) == type([]) and type(clave) == type("") and type(valor) == type("") and len(lista_heroes) > 0:
        lista_filtrada = []
        for heroe in lista_heroes:
            if heroe[clave] == valor:
                lista_filtrada.append(heroe)
                
        return lista_filtrada

def proyectar_clave(lista_heroes: list, clave: str, con_repe: bool = False) -> list:
    """
    Brief: Agrega una clave determinada de los diccionarios de la lista que le pasas a una lista nueva con solo esas claves, puede estar repetida o no, depende los parametros
    
    Parameters:
        lista_heroes: list -> La lista de diccionarios que quiero filtrar
        clave: str -> La clave que quiero que sea la lista nueva
        con_repe: bool -> es opcional, si esta en "False" imprime sin repetida, si esta en "True" imprime con la clave repetida(predeterminado: False)
        
    Return: Retorna la lista filtrada
    """
    
    
    if type(lista_heroes) == type([]) and type(clave) == type("") and len(lista_heroes) > 0:
        
        lista_filtrada = []
        
        for heroe in lista_heroes:
            lista_filtrada.append(heroe[clave])
        
        if not con_repe:
            
            lista_filtrada = sacar_repetidos(lista_filtrada)
        
        return lista_filtrada

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

def cantidad_personajes_tipo(lista_heroes: list, clave: str):
    """
    Brief: Muestra la cantidad de heroes que tiene cada tipo de algo (En caso de no tener, ingresa "No Tiene")
    
    Parameters:
    
    Return:
    """
    if type(lista_heroes) == type([]) and len(lista_heroes) > 0:
        lista_tipos = proyectar_clave(lista_heroes, clave)

        for elemento in lista_tipos:
            elemento = 0
            for heroe in lista_heroes:
                pass
    # MAAAAAAL





def listar_agrupados_tipo(lista_heroes: list, clave: str) -> None:
    """
    Brief: Muestra el nombre de los heroes separados en grupos segun la clave que le pases
    
    Parameters:
        lista_heroes: list -> La lista de diccionario que queres separar
        clave: str -> La clave del diccionario segun quieras agrupar
    
    Return: No retorna nada, imprime
    """
    if(type(lista_heroes) == type([]) and type(clave) == type("") and len(lista_heroes) > 0):
        lista_tipos = proyectar_clave(lista_heroes, clave)
        
        for tipo in lista_tipos:
            print(tipo)
            for heroe in lista_heroes:
                if heroe[clave] == tipo:
                    print(heroe["nombre"])
            print("------------------------------")

# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).

lista_masculinos = filtrar_heroe(lista_copiada, "genero", "M")
lista_femeninos = filtrar_heroe(lista_copiada, "genero", "F")

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
            lista_nombres_masculinos = proyectar_clave(lista_masculinos, "nombre")
            mostrar_lista(lista_nombres_masculinos, " Nombres masculinos")
        case "2":
            lista_nombres_femeninos = proyectar_clave(lista_femeninos, "nombre")
            mostrar_lista(lista_nombres_femeninos, " Nombres femeninos")
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
            listar_agrupados_tipo(lista_copiada, "color_ojos") # PREGUNTAR COMO HACER PARA QUE SE ME JUNTEN LOS DEL Blue y blue
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
            l1 = proyectar_clave(lista_copiada, "color_ojos", True)
            l2 = proyectar_clave(lista_copiada, "color_ojos", False)
            mostrar_lista(l1, "OJOS CON REPETICION")
            mostrar_lista(l2, "OJOS SIN REPETICION")
    
    os.system("pause")
