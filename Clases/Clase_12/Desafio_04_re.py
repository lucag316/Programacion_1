from data_stark import lista_personajes
import re
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
#---------------------------------------------------------------------1.1
def extraer_iniciales(nombre_heroe: str) -> str:
    """
    Brief: Se le pasa por parametro un nombre, se extraen las iniciales y se le agrega un punto, si el nombre contiene "the", se omite, solo si contiene guion se le reemplaza por un espacio, se valida que no este vacio el  string recibido
    
    Parameters:
        nombre_heroe: str -> El nombre del heroe que se le  extraeran las iniciales
    
    Return: Devuelve un nuevo string con las iniciales del nombre seguido de puntos, en caso de no cumplirse la validacion devuelve "N/A"
    """


# personaje = lista_personajes[0]
# print(extraer_iniciales(personaje["nombre"]))

#---------------------------------------------------------------------1.2

def definir_iniciales_nombre(heroe: dict) -> bool:
    """
    Brief: Agrega una nueva clave llamada "iniciales" al diccionario recibido, reutiliza la funcion: extraer_iniciales(), se valida que el dato sea dict y el diccionario contenga la clave nombre
    
    Parameters:
        heroe: dict -> El dicionario al que le quiero agregar la  clave
        
    Return: Si encuentra algun error retorna False, caso contrario retorna True
    """

# personaje = lista_personajes[0]
# print(definir_iniciales_nombre(personaje))

#---------------------------------------------------------------------1.3
def agregar_iniciales_nombre(lista_heroes: list) -> bool:
    """
    Brief: Itera la lista y le pasa a cada heroe la funcion: definir_iniciales_nombre(), si esa funcion retorna False se detiene la iteracion e informa por pantalla el siguiente mensaje:
    "El origen de datos no contiene el formato correcto"
    
    Parameters:
        lista_heroes: list -> La lista a la que le quiero agregar la clave
    
    Return: Devuelve True si finaliza con exito, False en caso de error
    """


#print(agregar_iniciales_nombre(lista_personajes))


#---------------------------------------------------------------------1.3
def stark_imprimir_nombres_con_iniciales(lista_heroes: list):
    """
    Brief: reutiliza la funcion: agregar_iniciales_nombre() para añadirle las iniciales a los diccionarios de la lista
    
    Parameters: 
        lista_heroes: list -> La lista que quiero utilizar
    
    Return: No retorna, imprime la lista completa de los nombres seguido de las iniciales entre parentesis
    """


#stark_imprimir_nombres_con_iniciales(lista_personajes)

#---------------------------------------------------------------------2.1
def generar_codigo_heroe(id_heroe: int, genero_heroe: str) -> str:
    """
    Brief: 
    
    Parameters: 
        id_heroe: int -> representa el identificador del heroe
        genero_heroe: str -> representa el genero del heroe "M", "F" o "NB"

    Return: En caso de no pasar las validaciones retorna "N/A". En caso de verificarse correctamente retorna el código generado
    """


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


#print(agregar_codigo_heroe(lista_personajes[0], 5555))


def stark_generar_codigos_heroes(lista_heroes: list):
    """
    """


#stark_generar_codigos_heroes(lista_personajes)





