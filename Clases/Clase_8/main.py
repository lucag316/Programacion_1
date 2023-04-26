from data_stark import lista_personajes

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






def filtrar(lista, clave, valor_que_quiero):
    lista_nueva = []
    for elemento in lista:
        if elemento[clave] == valor_que_quiero:
            lista_nueva.append(elemento)
    return lista_nueva

def proyectar_clave(lista, clave):
    lista_nueva_nombres = []
    for elemento in lista:
        lista_nueva_nombres.append(elemento[clave])
        
    return lista_nueva_nombres

l = filtrar(lista_personajes, "genero", "F") # todos la lista de dict femeninos
l2 = proyectar_clave(l, "nombre") #solo los nombres de la lista  l

#print(l)
#print(l2)

mostrar_lista(l2, "NOMBRES FEMENINOS")