# Desafío #02: (con biblioteca propia: stark_biblioteca)

from data_stark import lista_personajes
import os

#---------------------------------------------------------------------0
def stark_normalizar_datos(lista_heroes: list):
    """
    Brief: Convierte al tipo de dato correcto las claves de los diccionarios de la lista que se le pasa, si al menos un dato fue modificado se imprime 'Datos nomalizados', caso contrario no imprime nada
    
    Parameters:
        lista_heroes: list -> La lista que se quiere normalizar
        
    Return: No retorna nada, imprime si al menos un dato se normalizo
    """
    if len(lista_heroes) > 0:
    
        for heroe in lista_heroes:
            if type(heroe["altura"]) or type(heroe["peso"]) != type(float()):
                heroe["altura"] = float(heroe["altura"])
                heroe["peso"] = float(heroe["peso"])
                mensaje = "datos normalizados"
                
            if type(heroe["fuerza"]) != type(int()):
                heroe["fuerza"] = int(heroe["fuerza"])
                mensaje = "datos normalizados"
    else:
        mensaje = "ERROR, Lista de heroes vacia"
    print(mensaje)
stark_normalizar_datos(lista_personajes)

#---------------------------------------------------------------------1.1
def obtener_nombre(heroe: dict) -> str:
    """
    Brief: Obtiene el valor de la clave nombre del diccionario que le paso
    
    Parameters:
        heroe: dict -> el diccionario del heroe

    Return: Devuelve un string formateado, ej: (Nombre: Howard the Duck)
    """
    nombre = heroe["nombre"]
    mensaje = f"Nombre: {nombre}"
    return mensaje

#---------------------------------------------------------------------1.2
def imprimir_dato(cadena: str):
    """
    Brief: Imprime el string que se pasa por parametro
    
    Parameters:
        cadena: str -> el string que quiero imprimir

    Return: No retorna. imprime
    """
    print(cadena)

#---------------------------------------------------------------------1.3
def stark_imprimir_nombres_heroes(lista_heroes: list):
    """
    Brief: Imprime los nombres de la lista de heroes, reutiliza la funciones: obtener_nombre() e imprimir_dato()
    
    Parameters:
        lista_heroes: list -> La lista que quiero imprimir
    
    Return: No retorna, imprime la lista y -1 en caso de error
    """
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            nombre = obtener_nombre(heroe)
            imprimir_dato(nombre)
    else:
        return imprimir_dato("-1")         # aca dice: caso contrario no hará nada y retornara -1.(no se si esta bien porque enrealidad no retorna, imprime)

#---------------------------------------------------------------------2
def obtener_nombre_y_dato(heroe: dict,  key: str) -> str:
    """
    Brief: La funcion obtiene el nombre y una clave mas del diccionario, reutiliza la funcion: obtener_nombre()
    
    Parameters:
        heroe: dict -> El diccionario que se quieren obtener tales datos
        key: str -> El dato que se quiere obtener(ademas del nombre)
        
    Return: Devuele un string con el nombre y el dato
    """
    nombre = obtener_nombre(heroe)
    dato = heroe[key]
    mensaje = f"{nombre} | {key}: {dato}"
    return mensaje

#---------------------------------------------------------------------3
def stark_imprimir_nombres_alturas(lista_heroes: list):
    """
    Brief: Itera la lista e imprime los nombres y alturas, reutiliza la funcion: obtener_nombre_y_dato()
    
    Parameters:
        lista_heroes: list -> La lista que se quiere iterar
    
    Return: No retorna, imprime la lista o -1 en caso de error
    """
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            print(obtener_nombre_y_dato(heroe, "altura"))
    else:
        return print("-1")

#---------------------------------------------------------------------4.1
def calcular_max(lista_heroes: list, key: str) -> dict:
    """
    Brief: Calcula el maximo segun la  key  que se le pase
    
    Parameters:
        lista_heroes: list -> La  lista de diccionarios en la que quiere calcular
        key: str -> La clave con la que quiere hacer este calculo
    
    Return: Devuelve el maximo de la lista
    """
    max = lista_heroes[0]
    for heroe in lista_heroes:
        if heroe[key] > max[key]:
            max = heroe
    return max

#---------------------------------------------------------------------4.2
def calcular_min(lista_heroes: list, key: str) -> dict:
    """
    Brief: Calcula el minimo segun la  key  que se le pase
    
    Parameters:
        lista_heroes: list -> La  lista de diccionarios en la que quiere calcular
        key: str -> La clave con la que quiere hacer este calculo
    
    Return: Devuelve el minimo de la lista
    """
    min = lista_heroes[0]
    for heroe in lista_heroes:
        if heroe[key] < min[key]:
            min = heroe
    return min

#---------------------------------------------------------------------4.3
def calcular_max_min_dato(lista_heroes: list, tipo_calculo: str, key: str) -> dict:
    """
    Brief: Calcula el maximo o el minimo de la key que se le pase, reutiliza las funciones: calcular_max() y calcular_min
    
    Parameters:
        lista_heroes: list -> La  lista de diccionarios en la que quiere calcular
        tipo_calculo: str -> El tipo de calculo que se quiere hacer: "max" o "min"
        key: str -> La clave con la que quiere hacer este calculo
    
    Return: Devuelve el maximo o el minimo de la lista segun que se ingrese
    """
    if tipo_calculo == "max":
        max_min = calcular_max(lista_heroes, key)
    if tipo_calculo == "min":
        max_min = calcular_min(lista_heroes, key)
        
    return max_min

#---------------------------------------------------------------------4.4
def stark_calcular_imprimir_heroe(lista_heroes: list, tipo_calculo: str, key: str):
    """
    Brief: Obtiene el heroe que cumple con los parametros pedidos, reutiliza las funciones: imprimir_dato() y calcular_max_min_dato()
    
    Parameters:
        lista_heroes: list -> La lista que
        tipo_calculo: str -> El tipo de calculo que se quiere hacer: "max" o "min"
        key: str ->La clave con la que quiero calcular
        
    Return: si la lista esta vacia retorna -1
    """
    if len(lista_heroes) > 0:
        heroe = calcular_max_min_dato(lista_heroes, tipo_calculo, key)
        imprimir_dato("(condicion): Nombre: {0} | {1}: {2}".format(heroe["nombre"], key, heroe[key]))   # averiguar como se pone (condicion)
    else:
        return -1

#---------------------------------------------------------------------5.1
def sumar_dato_heroe(lista_heroes: list, key: str) -> float: 
    """
    Brief: Suma los datos de los heroes segun la key que se pase por parametro, antes de calcular se valida que el  heroe sea dict y que no este vacio
    
    Parameters:
        lista_heroes: list -> La lista en la que se quiere calcular
        key: str -> El dato de los heroes que se quiere sumar
    
    Return: Devuelve la suma de todos los datos segun la key pasada por parametro
    """
    # en realidad puede devolver int o float
    suma = 0
    
    for heroe in lista_heroes:
        if type(heroe) == type({}) and heroe != "": # tambien se puede poner type(dict()), es lo mismo
            suma += heroe[key]
        else:
            suma = -1
        
        # if(type(heroe) != type(dict()) or heroe == ""): # esta es otra forma que se puede hacer
        #     suma = -1
        # else:
        #     suma += float(heroe[key])
            
    return suma

#---------------------------------------------------------------------5.2
def dividir(dividendo: int, divisor: int) -> float:
    """
    Brief: Realiza una division entre los dos numeros que se ingresan
    
    Parameters: 
        dividendo: int -> Numero que se quiere dividir
        divisor: int -> Numero por el que se divide
    
    Return: Devuelve el resultado de la division o 0 en caso de que el divisor sea 0
    """
    if divisor == 0:
        retorno = 0
    else:
        retorno = dividendo / divisor
        
    return retorno

#---------------------------------------------------------------------5.3
def calcular_promedio(lista_heroes: list, key: str) -> float:
    """
    Brief: Calcula el promedio segun los parametros que se ingresan, reutiliza las funciones: sumar_dato_heroe() y dividir()
    
    Parameters: 
        lista_heroes: list -> La lista en la que se quiere calcular
        key: str -> El dato que se quiere calcular
    
    Return: Devuelve el promedio del dato pasado por parametro
    """
    suma = sumar_dato_heroe(lista_heroes, key)
    cantidad_heroes = len(lista_heroes)
    
    promedio = dividir(suma, cantidad_heroes)
        
    return promedio

#---------------------------------------------------------------------5.4
def stark_calcular_imprimir_promedio_altura(lista_heroes: list):
    """
    Brief: Calcula y muestra la altura promedio, valida que la lista no este vacia para realizar sus acciones, caso contrario no hace nada y retorna -1. Reutiliza las funciones: imprimir_dato(), sumar_dato_heroe() y calcular_promedio()
    
    Parameters: 
        lista_heroes: list -> la lista sobre la que se quiere calcular 
    
    Return: No retorna, imprime la altura promedio o -1                    
    """
    # ver como hacer que sea un RETORNO el -1                       # FALTA USAR LA FUNCION sumar_dato_heroe() QUE LO PIDE LA CONSIGNA, YA ESTA BIEN HECHO IGUAL
    if len(lista_heroes) > 0:
        promedio = calcular_promedio(lista_heroes, "altura")
        imprimir_dato(promedio)
    else:
        return print(-1)

#---------------------------------------------------------------------6.1
def imprimir_menu():
    imprimir_dato("""
        =========================================
            ***** MENU DE OPCIONES *****
        =========================================
        1- Imprimir nombres de los personajes 
        2- Imprimir nombres y alturas 
        3- Personaje mas alto
        4- Personaje mas bajo
        5- Personaje mas pesado
        6- Personaje mas liviano
        7- Personaje mas fuerte
        8- Personaje mas debil
        9- Promedio altura
        10- Promedio peso
        11- Promedio fuerza
        12- Salir
        =========================================
            """)

#---------------------------------------------------------------------6.2
def validar_entero(numero_str: str) -> bool:
    """
    Brief: Verifica que el numero pasado por parametro sea un string conformado solo por digitos
    
    Parameters: 
        numero_str: str -> El numero que sea un str
        
    Return: Retorna True si solo tiene diigitos, False caso contrario
    """
    if numero_str.isdigit():
        retorno = True
    else:
        retorno = False
        
    return retorno

#---------------------------------------------------------------------6.3
def stark_menu_principal() -> int:
    """
    Brief: Se encarga de  imprimir el menu de opciones, pide al usuario que ingrese el numero de la opcion elegida y lo valida. Reutiliza las funciones: imprimir_menu() y validar_entero()
    
    Parameters: No tiene parametros
    
    Return: En caso de ser correcto el numero, lo retorna casteado a entero, caso contrario retorna -1
    """
    imprimir_menu()
    
    opcion = (input("Ingrese una opcion: "))
    opcion_validada = validar_entero(opcion)
    
    if opcion_validada:
        retorno = int(opcion_validada)
    else:
        retorno = -1
    
    return retorno

#---------------------------------------------------------------------7
def stark_marvel_app(lista_heroes: list):
    """
    Brief: Se encarga de la ejecucion principal del programa, informa por consola si se selecciono una opcion incorrecta y vuelve a pedir el dato al usuario. Reutiliza las funciones: stark_menu_principal(), stark_imprimir_nombres_heroes(), stark_imprimir_nombres_alturas(), stark_calcular_imprimir_heroe(), stark_calcular_imprimir_promedio_altura(), calcular_promedio()
    
    Parameters: 
        lista_heroes: list -> La lista  que se desea utilizar
    
    Return: No tiene retorno, imprime segun la opcion que se seleccione
    """
    
    # agregue la funcion calcular_promedio() aunque no empieza con "stark"
    os.system("cls")
    while True:
        opcion = stark_menu_principal()
        match(opcion):
            case 1:
                stark_imprimir_nombres_heroes(lista_personajes)
            case 2:
                stark_imprimir_nombres_alturas(lista_personajes)
            case 3:
                print(stark_calcular_imprimir_heroe(lista_personajes, "max", "altura"))
            case 4:
                print(stark_calcular_imprimir_heroe(lista_personajes, "min", "altura"))
            case 5:
                print(stark_calcular_imprimir_heroe(lista_personajes, "max", "peso"))
            case 6:
                print(stark_calcular_imprimir_heroe(lista_personajes, "min", "peso"))
            case 7:
                print(stark_calcular_imprimir_heroe(lista_personajes, "max", "Fuerza"))
            case 8:
                print(stark_calcular_imprimir_heroe(lista_personajes, "min", "Fuerza"))
            case 9:
                stark_calcular_imprimir_promedio_altura(lista_personajes)
            case 10:
                print(calcular_promedio(lista_personajes, "peso"))
            case 11:
                print(calcular_promedio(lista_personajes, "fuerza"))
            case 12:
                confirmacion = input("Esta seguro? s/otra tecla: ")
                if confirmacion == "s":
                    break
                else: 
                    pass
            case _:
                print("Opcion incorrecta, vuelve a ingresar el dato: ")
        os.system("pause")

stark_marvel_app(lista_personajes)