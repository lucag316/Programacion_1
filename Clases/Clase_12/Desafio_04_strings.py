from data_stark import lista_personajes
"""
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
"""
lista_personajes_nueva = []
for heroe in lista_personajes:
    lista_personajes_nueva.append(heroe.copy())
#---------------------------------------------------------------------1.1
def extraer_iniciales(nombre_heroe: str) -> str:
    """
    Brief: Se le pasa por parametro un nombre, se extraen las iniciales y se le agrega un punto, si el nombre contiene "the", se omite, solo si contiene guion se le reemplaza por un espacio, se valida que no este vacio el  string recibido
    
    Parameters:
        nombre_heroe: str -> El nombre del heroe que se le  extraeran las iniciales
    
    Return: Devuelve un nuevo string con las iniciales del nombre seguido de puntos, en caso de no cumplirse la validacion devuelve "N/A"
    """
    retorno = "N/A"
    iniciales = ""
    if(nombre_heroe != ""):
        nombre_heroe = nombre_heroe.upper()
        if "-" in nombre_heroe:
            nombre_heroe = nombre_heroe.replace("-", " ")
        if "THE" in nombre_heroe:
            nombre_heroe = nombre_heroe.replace("THE", "")
            
        nombre_heroe = nombre_heroe.strip()
        nombre_heroe = nombre_heroe.split(" ")
        
        for parte in nombre_heroe:
            if parte != "":
                iniciales = iniciales + parte[0] + "."
        retorno = iniciales

    return retorno
#print(extraer_iniciales(""))

#---------------------------------------------------------------------1.2
def definir_iniciales_nombre(heroe: dict) -> bool:
    """
    Brief: Agrega una nueva clave llamada "iniciales" al diccionario recibido, reutiliza la funcion: extraer_iniciales(), se valida que el dato sea dict y el diccionario contenga la clave nombre
    
    Parameters:
        heroe: dict -> El dicionario al que le quiero agregar la  clave
        
    Return: Si encuentra algun error retorna False, caso contrario retorna True
    """
    retorno = False
    if type(heroe) == type({}) and "nombre" in heroe:
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
        retorno = True
    return retorno

# personaje = lista_personajes_nueva[0]
# print(definir_iniciales_nombre(personaje))
# print(lista_personajes_nueva)

#---------------------------------------------------------------------1.3
def agregar_iniciales_nombre(lista_heroes: list) -> bool:
    """
    Brief: Itera la lista y le pasa a cada heroe la funcion: definir_iniciales_nombre(), si esa funcion retorna False se detiene la iteracion e informa por pantalla el siguiente mensaje:
    "El origen de datos no contiene el formato correcto"
    
    Parameters:
        lista_heroes: list -> La lista a la que le quiero agregar la clave
    
    Return: Devuelve True si finaliza con exito, False en caso de error
    """
    retorno = False
    if type(lista_heroes) == type([]) and len(lista_heroes) > 0:
        for heroe in lista_heroes:
            heroe_booleano = definir_iniciales_nombre(heroe)
            retorno = True
            if heroe_booleano == False:
                print("El origen de datos no contiene el formato correcto")
                retorno = False
                break
    return retorno

#print(agregar_iniciales_nombre(lista_personajes_nueva))

#---------------------------------------------------------------------1.3
def stark_imprimir_nombres_con_iniciales(lista_heroes: list):
    """
    Brief: reutiliza la funcion: agregar_iniciales_nombre() para añadirle las iniciales a los diccionarios de la lista
    
    Parameters: 
        lista_heroes: list -> La lista que quiero utilizar
    
    Return: No retorna, imprime la lista completa de los nombres seguido de las iniciales entre parentesis
    """
    if type(lista_heroes) == type([]) and len(lista_heroes) > 0:
        agregar_iniciales_nombre(lista_heroes)
        for heroe in lista_heroes:
            print("* {0}({1})".format(heroe["nombre"], heroe["iniciales"]))

#stark_imprimir_nombres_con_iniciales(lista_personajes_nueva)

#---------------------------------------------------------------------2.1
def generar_codigo_heroe(id_heroe: int, genero_heroe: str) -> str:
    """
    Brief: 
    
    Parameters: 
        id_heroe: int -> representa el identificador del heroe
        genero_heroe: str -> representa el genero del heroe "M", "F" o "NB"

    Return: En caso de no pasar las validaciones retorna "N/A". En caso de verificarse correctamente retorna el código generado
    """
    retorno = "N/A"
    if type(id_heroe) == type(int()) and genero_heroe != "" and genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB":
        relleno = 9 - len(genero_heroe)                            # creo que seria mejor relleno = 10 - (len(genero_heroe) + 1) o por lo menos es otra forma
        id_nuevo = str(id_heroe).zfill(relleno)
        retorno = "{0}-{1}".format(genero_heroe, id_nuevo)
    return retorno

# print(generar_codigo_heroe(155557, "M"))
# print(generar_codigo_heroe(85, "NB"))

#---------------------------------------------------------------------2.2
def agregar_codigo_heroe(heroe: dict, id_heroe: int) -> bool:
    """
    Brief: Agrega una nueva clave llamada "codigo_heroe" al diccionario del personaje, le asigna como valor un codigo utilizando la funcion  "generar_codigo_heroe"
    
    Parameters: 
        heroe: dict -> Un diccionario con los datos del personaje
        id_heroe: int -> Un entero que representa el identificador del heroe
    
    Return: En caso de pasar las validaciones correctamente la función retorna True, en caso de encontrarse un error retorna False
    """
    retorno = False
    codigo = generar_codigo_heroe(id_heroe, heroe["genero"])
    if heroe != "" and len(codigo) == 10:
        heroe["codigo_heroe"] = codigo
        retorno = True
    return retorno
#print(agregar_codigo_heroe(lista_personajes[0], 5555))

#---------------------------------------------------------------------2.3
def stark_generar_codigos_heroes(lista_heroes: list):
    """
    Brief: La funcion itera la lista agregando todos los codigos y los imprime por pantalla, reutiliza la  funcion: agregar_codigo_heroe()
    
    Parameters: 
        lista_heroes: list -> La lista que se  desea utilizar
        
    Return: no retorna, imprime los codigos de esta manera: * El codigo del heroe es: M-00000001, En caso de encontrar algún error, informa por pantalla: "El origen de datos no contiene el formato correcto"
    """
    # no esta bien lo que se imprime(ver)
    contador_id = 0
    if len(lista_heroes):
        for heroe in lista_heroes:
            if type(heroe) == type({}) and "genero" in heroe:
                contador_id += 1
                agregar_codigo_heroe(heroe, contador_id)
                print("* El codigo del heroe es: {0}".format(heroe["codigo_heroe"]))
            else:
                print("El origen de datos no contiene el formato correcto")
                break
        print("Se asignaron {0} codigos".format(contador_id))
    else:
        print("El origen de datos no contiene el formato correcto")

# lista = [1, 2]
# stark_generar_codigos_heroes(lista)

#---------------------------------------------------------------------3.1
def sanitizar_entero(numero_str: str) -> int:
    """
    Brief: Determina si es un entero positivo, saca los espacios en blanco si tiene
    
    Parameters:
        numero_str: str -> un string que representa un posible entero
    Return: 
        Si lo que se introduzco fue un string y el contenido es un entero positivo, lo retorna en un entero
        -1 si contiene caracteres no numericos
        -2 si el numero es negativo
        -3 si ocurren otros errores que no permiten convertirlo a entero
    """
    # if numero_str[0] == "-" and numero_str[1:].isdigit():          # primer lugar un menos y despues numeros
    #     retorno = -4
    
    
    if type(numero_str) == type(str()):
        numero_str = numero_str.strip()
        if numero_str[0] == "-" and not numero_str[1:].isdigit():
            retorno = -1
        elif numero_str[0] == "-" and numero_str[1:].isdigit():
            retorno = -2
        elif numero_str.isdigit():
            numero = int(numero_str)
            retorno = numero
    else:
        retorno = -3
        
    return retorno                                        # arreglar porque se rompe si le pongo desde el indice 0 un caracter que no sea  - o numero
    #--------------------------------------------------
    # if type(numero_str) == type(str()):
    #     numero_str = numero_str.strip()
    #     if not numero_str.isdigit():
    #         retorno = -1
    #     else:
    #         numero_int = int(numero_str)
    #         if numero_int < 0:
    #             retorno = -2
    #         else:
    #             retorno = numero_int
    # else:
    #     retorno = -3
        
    # return retorno
    # ---------------------------
    # if type(numero_str) == type(str()):
    #     numero_str = numero_str.strip()
    #     if not numero_str.isdigit():
    #         retorno = -1
    #     elif numero_str.startswith("-"):
    #         retorno = -2
    #     else:
    #         try:
    #             numero = int(numero_str)
    #             if numero < 0:
    #                 retorno = -2
    #             else: 
    #                 retorno = numero
    #         except:
    #             retorno -3
    # else:
    #     retorno = -3
        
    # return retorno            #sigue faltando el -2 que este bien

#print(sanitizar_entero(46))

def sanitizar_flotante(numero_str: str) -> float:
    """
    Brief: Determina si es un flotante positivo, saca los espacios en blanco si tiene
    
    Parameters:
        numero_str: str -> un string que representa un posible decimal
    Return: 
        Si lo que se introduzco fue un string y el contenido es un flotante positivo, lo retorna en un flotante
        -1 si contiene caracteres no numericos
        -2 si el numero es negativo
        -3 si ocurren otros errores que no permiten convertirlo a flotante
    """
    # if numero_str[0] == "-" and numero_str[1:].isdigit():          # primer lugar un menos y despues numeros
    #     retorno = -4
    
    
#     if type(numero_str) == type(str()):
#         numero_str = numero_str.strip()
#         if numero_str[0] == "-" and not numero_str[1:].isdigit():
#             retorno = -1
#         elif numero_str[0] == "-" and numero_str[1:].isdigit():
#             retorno = -2
#         elif numero_str.isdigit():
#             numero = float(numero_str)
#             retorno = numero
#     else:
#         retorno = -3
        
#     return retorno                                        # arreglar porque se rompe si le pongo desde el indice 0 un caracter que no sea  - o numero
# print(sanitizar_flotante("0.2"))


def sanitizar_string(valor_str: str, valor_por_defecto: str = "-"):
    """
    Brief: Determina si es solo texto(sin numeros)
    
    Parameters:
        valor_str: str -> Representa el texto a validar
        valor_por_defecto: str -> Representa un valor por defecto (parámetro opcional, inicializado con "-")
    Return: 
        "N/A" si encuenta numeros
        si es solo texto, retorna lo mismo convertido en minusculas
        En el caso que el texto a validar se encuentre vacío y si se paso un valor por defecto, retorna el valor por defecto convertido a minusculas
    """
    retorno = "N/A"
    if type(valor_str) == type(str()):
        if valor_str[0] == " " or valor_str[-1] == " " or valor_por_defecto[0] == " " or valor_por_defecto[-1] == " ":
            valor_str = valor_str.strip()
            valor_por_defecto = valor_por_defecto.strip()
            
        if valor_str.isalpha():
            valor_str = valor_str.lower()
            retorno = valor_str
            
            if valor_str.count("/") > 0:
                valor_str = valor_str.replace("/", " ")
                
        if valor_str == "" and valor_por_defecto != "-":
            valor_por_defecto = valor_por_defecto.lower()
            retorno = valor_por_defecto
    
    return retorno                            # MAL, CORREGIR

print(sanitizar_string("hola/mundo", ""))





def sanitizar_dato():
    """
    Brief: 
    
    Parameters:
        d
    Return: 
    """






def stark_normalizar_datos():
    """
    Brief: 
    
    Parameters:
        d
    Return: 
    """






def stark_normalizar_datos():
    """
    Brief: 
    
    Parameters:
        d
    Return: 
    """













# from data_stark import lista_personajes
# #import re
# """
#     "nombre": "Howard the Duck",
#     "identidad": "Howard (Last name unrevealed)",
#     "empresa": "Marvel Comics",
#     "altura": "79.349999999999994",
#     "peso": "18.449999999999999",
#     "genero": "M",
#     "color_ojos": "Brown",
#     "color_pelo": "Yellow",
#     "fuerza": "2",
#     "inteligencia": ""
# """
# #---------------------------------------------------------------------1.1
# def extraer_iniciales(nombre_heroe: str) -> str:
#     """
#     Brief: Se le pasa por parametro un nombre, se extraen las iniciales y se le agrega un punto, si el nombre contiene "the", se omite, solo si contiene guion se le reemplaza por un espacio, se valida que no este vacio el  string recibido
    
#     Parameters:
#         nombre_heroe: str -> El nombre del heroe que se le  extraeran las iniciales
    
#     Return: Devuelve un nuevo string con las iniciales del nombre seguido de puntos, en caso de no cumplirse la validacion devuelve "N/A"
#     """
#     retorno = "N/A"
#     iniciales = ""

#     if(type(nombre_heroe) == type(str()) and len(nombre_heroe) > 0):
#         nombre_heroe = nombre_heroe.upper()
#         nombre_heroe = nombre_heroe.replace("THE ", "")

#         if(nombre_heroe.count("-") > 0):
#             nombre_heroe = nombre_heroe.replace("-", " ")

#         nombre_heroe = nombre_heroe.strip()
#         nombre_heroe = nombre_heroe.split(" ")
#         partes_nombre = nombre_heroe

#         for parte in partes_nombre:
#             iniciales += parte[0] + "."

#         retorno = iniciales
    
#     return retorno

# # personaje = lista_personajes[0]
# # print(extraer_iniciales(personaje["nombre"]))

# #---------------------------------------------------------------------1.2

# def definir_iniciales_nombre(heroe: dict) -> bool:
#     """
#     Brief: Agrega una nueva clave llamada "iniciales" al diccionario recibido, reutiliza la funcion: extraer_iniciales(), se valida que el dato sea dict y el diccionario contenga la clave nombre
    
#     Parameters:
#         heroe: dict -> El dicionario al que le quiero agregar la  clave
        
#     Return: Si encuentra algun error retorna False, caso contrario retorna True
#     """
#     retorno = False
#     if type(heroe) == type({}) and "nombre" in heroe:
        
#         iniciales = extraer_iniciales(heroe["nombre"])
#         heroe["iniciales"] = iniciales

#         retorno = True
    
#     return retorno
# # personaje = lista_personajes[0]
# # print(definir_iniciales_nombre(personaje))

# #---------------------------------------------------------------------1.3
# def agregar_iniciales_nombre(lista_heroes: list) -> bool:
#     """
#     Brief: Itera la lista y le pasa a cada heroe la funcion: definir_iniciales_nombre(), si esa funcion retorna False se detiene la iteracion e informa por pantalla el siguiente mensaje:
#     "El origen de datos no contiene el formato correcto"
    
#     Parameters:
#         lista_heroes: list -> La lista a la que le quiero agregar la clave
    
#     Return: Devuelve True si finaliza con exito, False en caso de error
#     """
#     #retorno = False # no se si tambien va aca
#     if type(lista_heroes) == type([]) and len(lista_heroes) > 0:
#         for heroe in lista_heroes:
#             heroe_extendido = definir_iniciales_nombre(heroe)
            
#             if heroe_extendido == False:
#                 print("El origen de datos no contiene el formato correcto")
#                 retorno = False
#                 break
#             else:
#                 retorno = True
#     return retorno

# #print(agregar_iniciales_nombre(lista_personajes))


# #---------------------------------------------------------------------1.3
# def stark_imprimir_nombres_con_iniciales(lista_heroes: list):
#     """
#     Brief: reutiliza la funcion: agregar_iniciales_nombre() para añadirle las iniciales a los diccionarios de la lista
    
#     Parameters: 
#         lista_heroes: list -> La lista que quiero utilizar
    
#     Return: No retorna, imprime la lista completa de los nombres seguido de las iniciales entre parentesis
#     """
#     if type(lista_heroes) == type([]) and len(lista_heroes) > 0:
#         agregar_iniciales_nombre(lista_heroes)
        
#         for heroe in lista_heroes:
#             print(f"* {heroe['nombre']} ({heroe['iniciales']})")

# #stark_imprimir_nombres_con_iniciales(lista_personajes)

# #---------------------------------------------------------------------2.1
# def generar_codigo_heroe(id_heroe: int, genero_heroe: str) -> str:
#     """
#     Brief: 
    
#     Parameters: 
#         id_heroe: int -> representa el identificador del heroe
#         genero_heroe: str -> representa el genero del heroe "M", "F" o "NB"

#     Return: En caso de no pasar las validaciones retorna "N/A". En caso de verificarse correctamente retorna el código generado
#     """
#     if type(id_heroe) == type(int()) and genero_heroe != "" and genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB":
#         relleno = 10 - (len(genero_heroe) + 1)
#         id_nuevo = str(id_heroe).zfill(relleno)
        
#         retorno = f"{genero_heroe}-{id_nuevo}"
#     else:
#         retorno = "N/A"
        
#     return retorno

# # print(generar_codigo_heroe(155557, "M"))
# # print(generar_codigo_heroe(85, "NB"))

# #---------------------------------------------------------------------2.2
# def agregar_codigo_heroe(heroe: dict, id_heroe: int) -> bool:
#     """
#     Brief: Agrega una nueva clave llamada "codigo_heroe" al diccionario del personaje, le asigna como valor un codigo utilizando la funcion  "generar_codigo_heroe"
    
#     Parameters: 
#         heroe: dict -> Un diccionario con los datos del personaje
#         id_heroe: int -> Un entero que representa el identificador del heroe
    
#     Return: En caso de pasar las validaciones correctamente la función retorna True, en caso de encontrarse un error retorna False
#     """
#     retorno = False
#     codigo = generar_codigo_heroe(id_heroe, heroe["genero"])
    
#     if heroe != "" and len(codigo) == 10:
#         heroe["codigo_heroe"] = codigo
#         retorno = True
        
#     return retorno

# #print(agregar_codigo_heroe(lista_personajes[0], 5555))


# def stark_generar_codigos_heroes(lista_heroes: list):
#     """
#     """
#     contador_id = 0
#     if len(lista_heroes) > 0:
#         for heroe in lista_heroes:
#             if type(heroe) == type({}) and "genero" in heroe:
                
#                 contador_id += 1
#                 agregar_codigo_heroe(heroe, contador_id)
#                 print("* El codigo del heroe es: {0}".format(heroe["codigo_heroe"]))           # SUPUESTAMENTE EN EL ENUNCIADO  DICE QUE TIENE QUE  DECIR, EL PRIMER HEROE, EL SEGUNDO Y ASI PERO NOSE

#         print(f"Se asignaron {contador_id} codigos")
#     else:
#         print("El origen de datos no contiene el formato correcto")

# stark_generar_codigos_heroes(lista_personajes)

























"""
    Brief: 
    
    Parameters: 

    Return: 
"""