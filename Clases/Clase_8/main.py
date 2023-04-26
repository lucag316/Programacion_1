from data_stark import lista_personajes

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
            print(elemento)
print(cantidad_personajes_tipo(lista_personajes, "color_ojos"))


# # # # # def calcular_tipo_inteligencia(lista_personajes:list):
# # # # #     '''
# # # # #     Calcula cuantos personajes son  de cada tipo de inteligencia

# # # # #     Recibe la lista de personajes
# # # # #     '''
# # # # #     tipo_inteligencia = {}
# # # # #     for personaje in lista_personajes:
# # # # #         if (personaje["inteligencia"] == ""):
# # # # #             tipo_inteligencia["No tiene"] = 0
# # # # #         else:   
# # # # #             tipo_inteligencia[personaje["inteligencia"]] = 0

# # # # #     for personaje in lista_personajes:
# # # # #         if (personaje["inteligencia"] == ""):
# # # # #             tipo_inteligencia["No tiene"] += 1
# # # # #         else:
# # # # #             tipo_inteligencia[personaje["inteligencia"]] += 1

# # # # #     print(tipo_inteligencia)
# # # # # #-----------------------------------------PUNTO L-------------------------------------------------------------------------











































# lista = []
# colores = []

# for heroe in lista_personajes:
#     lista.append(heroe.copy())
#     for clave in heroe:
#         color = clave["color_ojos"]
#         if color not in colores:
#             colores.append(color)
            
            
# for heroe in lista_personajes:
#     lista.append(heroe.copy())
    
# for heroe in lista:
#     colores.append(clave["color_ojos"])




###################################################



# lista_copiada = []
# for personaje in lista_personajes:
#     lista_copiada.append(personaje.copy())


# def crear_lista_femeninos(lista_heroes: list) -> list:
#     lista_femeninos = []
#     for heroe in lista_heroes:
#         if heroe["genero"] == "F":
#             lista_femeninos.append(heroe)
#     return lista_femeninos
# def crear_lista_masculinos(lista_heroes: list) -> list:
#     lista_masculinos = []
#     for heroe in lista_heroes:
#         if heroe["genero"] == "M":
#             lista_masculinos.append(heroe)
#     return lista_masculinos

# lista_femeninos = crear_lista_femeninos(lista_copiada)
# lista_masculinos = crear_lista_masculinos(lista_copiada)


# def calcular_max_min(lista_heroes: list, condicion: str, clave: str) -> dict:
#     """
#     brief: Calcula cual es el maximo o el minimo de una lista de diccionarios(depende de los parametros que ingreses)
    
#     Parameters: 
#         lista_heroes: list -> sobre la lista que voy a calcular
#         condicion: str -> ingresar ("max" o "min ") para buscar el mayor o menor de la lista
#         clave: str -> sobre lo que quiero calcular("altura", "peso", etc)
    
#     Return: Retorna el diccionario del heroe segun el calculo que se hizo
#     """
#     if(type(lista_heroes) == type([]) and type(condicion) == type("") and type(clave) == type("") and len(lista_heroes) > 0):
        
#         max_min = lista_heroes[0]
        
#         for heroe in lista_heroes:
#             if condicion == "max" and heroe[clave] > max_min[clave]:
#                 max_min = heroe
#             if condicion == "min" and heroe[clave] < max_min[clave]:
#                 max_min = heroe
            
#         return max_min
    
# print(lista_femeninos)
# print("---------------------")
# print(lista_masculinos)
# print("---------------------")

# print(calcular_max_min(lista_masculinos, "max", "altura"))
# print(calcular_max_min(lista_femeninos, "max", "altura"))
# print(calcular_max_min(lista_masculinos, "min", "altura"))
# print(calcular_max_min(lista_femeninos, "min", "altura"))


##########################################
# def mostrar_lista(lista: list, titulo: str) -> None:
#     """
#     Brief: Muestra la lista mas prolija con su item y con un titulo (como un print pero mas prolijo)
    
#     Parameters:
#         lista: list -> lista que quiero mostrar
#         titulo: str -> Titulo que le quiero poner a la lista
        
#     Return: No retorna nada, imprime
#     """
#     if type(lista) == type([]) and type(titulo) == type("") and len(lista) > 0:
#         print("--------------------------------------")
#         print(f"   ****** {titulo} *****")
#         print("--------------------------------------")
#         for item in lista:
#             print(item)
#         print("--------------------------------------")






# def filtrar(lista, clave, valor_que_quiero):
#     lista_nueva = []
#     for elemento in lista:
#         if elemento[clave] == valor_que_quiero:
#             lista_nueva.append(elemento)
#     return lista_nueva

# def proyectar_clave(lista, clave):
#     lista_nueva_nombres = []
#     for elemento in lista:
#         lista_nueva_nombres.append(elemento[clave])
        
#     return lista_nueva_nombres

# l = filtrar(lista_personajes, "genero", "F") # todos la lista de dict femeninos
# l2 = proyectar_clave(l, "nombre") #solo los nombres de la lista  l

# #print(l)
# #print(l2)

# mostrar_lista(l2, "NOMBRES FEMENINOS")