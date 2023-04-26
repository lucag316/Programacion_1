# Desafío #02: (con biblioteca propia: stark_biblioteca)
# En base a lo resuelto en el desafío #00, deberás mejorar la calidad de tus funciones. Es por ello que te proponemos lo siguiente:
# IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista, un string, etc y que contendrá) y que es lo que retorna la función!
# Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista de héroes. La función deberá:
# Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que representan datos numéricos)
# Validar primero que el tipo de dato no sea del tipo al cual será casteado. Por ejemplo si una key debería ser entero (ejemplo edad) verificar antes que no se encuentre ya en ese tipo de dato.
# Si al menos un dato fue modificado, la función deberá imprimir como mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”


# Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el cual representara a un héroe y devolverá un string el cual contenga su nombre formateado de la siguiente manera: 
# Nombre: Howard the Duck


# Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y deberá imprimirlo en la consola. La función no tendrá retorno.


# Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por parámetro la lista de héroes y deberá imprimirla en la consola. Reutilizar las funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Con este se resuelve el Ej 1 del desafío #00


# Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener. 


# La función deberá devolver un string el cual contenga el nombre y dato (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.


# El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza)
# Nombre: Venom | fuerza: 500


# Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por parámetro la lista de héroes, la cual deberá iterar e imprimir sus nombres y alturas USANDO la función creada en el punto 2. Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Con este se resuelve el Ej 2 del desafío #00
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
#---------------------------------------------------------------------0
def stark_normalizar_datos(lista_heroes: list):
    
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
    nombre = heroe["nombre"]
    mensaje = f"Nombre: {nombre}"
    return mensaje

obtener_nombre(lista_personajes[0])

#---------------------------------------------------------------------1.2
def imprimir_dato(cadena: str):
    print(cadena)

#---------------------------------------------------------------------1.3
def stark_imprimir_nombres_heroes(lista_heroes: list):
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            nombre = obtener_nombre(heroe)
            imprimir_dato(nombre)
            
stark_imprimir_nombres_heroes(lista_personajes)